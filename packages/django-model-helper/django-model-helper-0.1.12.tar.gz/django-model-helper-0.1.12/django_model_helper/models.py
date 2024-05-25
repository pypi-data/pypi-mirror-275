#!/usr/bin/env python
# -*- coding: utf8 -*-
import json
import uuid
import datetime
import logging

import yaml
from bizerror import BizError
from zenutils import jsonutils

from django.db import models
from django.db.models.aggregates import Max
from django.utils import timezone

from django_safe_fields.fields import SafeTextField

__all__ = [
    "WithAddModTimeFields",
    "WithEnabledStatusFields",
    "WithLockStatusFields",
    "WithDeletedStatusFields",
    "WithConfigFields",
    "WithDisplayOrderFields",
    "WithJsonDataFields",
    "WithUidFields",
    "WithSimpleNRRDStatusFields",
    "WithSimpleResultFields",
    "WithCountFields",
    "WithExpireTimeFields",
    "WithVisibleFields",
    "WithHotspotFields",
    "WithArgsKwargsFields",
]

_logger = logging.getLogger(__name__)


class WithAddModTimeFields(models.Model):
    """添加创建时间/修改时间相关字段。"""

    add_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="添加时间",
    )
    mod_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="修改时间",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.add_time is None:
            self.add_time = timezone.now()
        self.mod_time = timezone.now()
        return super().save(*args, **kwargs)


class WithEnabledStatusFields(models.Model):
    """添加启用状态相关字段。"""

    enabled = models.BooleanField(
        default=True,
        verbose_name="启用",
    )
    enabled_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="启用时间",
    )
    disabled_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="禁用时间",
    )

    class Meta:
        permissions = [
            ("set_enabled", "允许设置启用标记"),
            ("set_disabled", "允许设置禁用标记"),
        ]
        abstract = True

    def save(self, *args, **kwargs):
        if self.enabled:
            if self.enabled_time is None:
                self.enabled_time = timezone.now()
            if self.disabled_time is not None:
                self.disabled_time = None
        else:
            if self.enabled_time is not None:
                self.enabled_time = None
            if self.disabled_time is None:
                self.disabled_time = timezone.now()
        return super().save(*args, **kwargs)

    def set_enabled(self, save=True):
        self.enabled = True
        self.enabled_time = timezone.now()
        self.disabled_time = None
        if save:
            self.save()

    def set_disabled(self, save=True):
        self.enabled = False
        self.enabled_time = None
        self.disabled_time = timezone.now()
        if save:
            self.save()

    @property
    def is_enabled(self):
        return self.enabled

    def enabled_display(self):
        return self.enabled and "已启用" or "已禁用"

    enabled_display.short_description = "启用状态"


class WithLockStatusFields(models.Model):
    """添加锁定相关字段。"""

    lock = models.BooleanField(
        default=False,
        verbose_name="锁定",
    )
    locked_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="锁定时间",
    )
    unlocked_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="解锁时间",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.lock:
            if self.locked_time is None:
                self.locked_time = timezone.now()
            if self.unlocked_time is not None:
                self.unlocked_time = None
        else:
            if self.locked_time is not None:
                self.locked_time = None
            if self.unlocked_time is None:
                self.unlocked_time = timezone.now()
        return super().save(*args, **kwargs)

    def set_locked(self, save=True):
        self.lock = True
        if save:
            self.save()

    def set_unlocked(self, save=True):
        self.lock = False
        if self.save:
            self.save()

    @property
    def is_locked(self):
        return self.lock


class WithDeletedStatusFields(models.Model):
    """添加删除状态相关字段。"""

    deleted = models.BooleanField(
        default=False,
        verbose_name="是否已删除",
    )
    deleted_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="删除时间",
    )

    class Meta:
        permissions = [
            ("set_deleted", "允许设置删除标记"),
            ("set_undeleted", "允许清除删除标记"),
        ]
        abstract = True

    def save(self, *args, **kwargs):
        if self.deleted:
            if self.deleted_time is None:
                self.deleted_time = timezone.now()
        else:
            if self.deleted_time is not None:
                self.deleted_time = None
        return super().save(*args, **kwargs)

    def set_deleted(self, save=True):
        self.deleted = True
        if save:
            self.save()

    def set_undeleted(self, save=True):
        self.deleted = False
        if save:
            self.save()

    @property
    def is_deleted(self):
        return self.deleted

    def deleted_display(self):
        return self.deleted and "已删除" or "未删除"

    deleted_display.short_description = "删除标记"


class WithConfigFields(models.Model):
    is_config_valid = models.BooleanField(
        null=True,
        verbose_name="参数设置是否正确",
        help_text="保存后自动判定格式是否正确。",
        editable=False,
    )
    config_data = SafeTextField(
        null=True,
        blank=True,
        verbose_name="参数设置",
        help_text="参数设置格式为YAML格式。",
    )

    class Meta:
        abstract = True

    def get_config(self):
        if not self.config_data:
            return {}
        else:
            return yaml.safe_load(self.config_data)

    def set_config(self, data):
        self.config_data = yaml.safe_dump(data)

    config = property(get_config, set_config)

    def save(self, *args, **kwargs):
        try:
            self.config
            self.is_config_valid = True
        except Exception as error:
            _logger.error(
                "config数据格式非法：error=%s",
                error,
            )
            self.is_config_valid = False
        return super().save(*args, **kwargs)


class WithDisplayOrderFields(models.Model):
    display_order_offset = 10000
    display_order_increment = 100

    display_order = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="显示排序",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.display_order:
            self.display_order = self.get_next_display_order()
        return super().save(*args, **kwargs)

    @classmethod
    def get_next_display_order(cls):
        display_order__max = cls.objects.aggregate(Max("display_order")).get(
            "display_order__max"
        )
        if display_order__max is None:
            return cls.display_order_offset
        else:
            return display_order__max + cls.display_order_increment


class WithJsonDataFields(models.Model):
    data_raw = SafeTextField(
        null=True,
        blank=True,
        verbose_name="数据",
        help_text="JSON格式。",
    )

    class Meta:
        abstract = True

    def get_data(self):
        if not self.data_raw:
            return {}
        else:
            return json.loads(self.data_raw)

    def set_data(self, value):
        self.data_raw = jsonutils.simple_json_dumps(value, ensure_ascii=False)

    data = property(get_data, set_data)


class WithUidFields(models.Model):

    uid = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        verbose_name="唯一码",
    )

    class Meta:
        abstract = True

    @classmethod
    def uidgen(cls):
        return uuid.uuid4().hex

    def save(self, *args, **kwargs):
        if not self.uid:
            self.uid = self.uidgen()
        return super().save(*args, **kwargs)


class WithSimpleNRRDStatusFields(models.Model):
    """添加简易流程状态。

    状态列表：
        NEW
        READY
        RUNNING
        DONE
    状态转化方法：
        set_new
        set_ready
        start
        set_done
    状态转化流程：
        NEW --set_ready()--> READY --start()--> RUNNING --set_done()--> DONE

    状态值：
        NEW = 0 或 None
        READY = 10
        RUNNING 20
        DONE = 30

    默认情况下：
        对象在保存时，会自动进入READY状态。

    当设置类属性is_auto_ready=False时：
        对象在保存时，不会进入READY状态。

    """

    is_auto_ready = True

    NEW = 0
    READY = 10
    RUNNING = 20
    DONE = 30
    STATUS = [
        (NEW, "新建"),
        (READY, "就绪"),
        (RUNNING, "执行中"),
        (DONE, "完成"),
    ]

    status = models.IntegerField(
        choices=STATUS,
        null=True,
        blank=True,
        verbose_name="状态",
    )
    ready_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="就绪时间",
    )
    start_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="开始时间",
    )
    done_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="完成时间",
    )

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.status is None:
            if self.is_auto_ready:
                self.status = self.READY
            else:
                self.status = self.NEW
        if self.status == self.NEW:
            if self.ready_time is not None:
                self.ready_time = None
            if self.start_time is not None:
                self.start_time = None
            if self.done_time is not None:
                self.done_time = None
        if self.status == self.READY:
            if self.ready_time is None:
                self.ready_time = timezone.now()
            if self.start_time is not None:
                self.start_time = None
            if self.done_time is not None:
                self.done_time = None
        elif self.status == self.RUNNING:
            if self.ready_time is None:
                self.ready_time = timezone.now()
            if self.start_time is None:
                self.start_time = timezone.now()
            if self.done_time is not None:
                self.done_time = None
        elif self.status == self.DONE:
            if self.ready_time is None:
                self.ready_time = timezone.now()
            if self.start_time is None:
                self.start_time = timezone.now()
            if self.done_time is None:
                self.done_time = timezone.now()
        return super().save(*args, **kwargs)

    def set_new(self, save=True):
        self.status = self.NEW
        self.ready_time = None
        self.start_time = None
        self.done_time = None
        if self.save:
            return self.save()

    def set_ready(self, save=True):
        self.status = self.READY
        self.ready_time = timezone.now()
        self.start_time = None
        self.done_time = None
        if self.save:
            self.save()

    def start(self, save=True):
        self.status = self.RUNNING
        self.ready_time = None
        self.start_time = timezone.now()
        self.done_time = None
        if save:
            self.save()

    def set_done(self, save=True):
        self.status = self.DONE
        self.ready_time = None
        self.start_time = None
        self.done_time = timezone.now()
        if save:
            self.save()

    @property
    def is_new(self):
        return (self.status == self.NEW) or (self.status is None)

    @property
    def is_ready(self):
        return self.status == self.READY

    @property
    def is_running(self):
        return self.status == self.RUNNING

    @property
    def is_done(self):
        return self.status == self.DONE


class WithSimpleResultFields(models.Model):
    success = models.BooleanField(
        null=True,
        blank=True,
        verbose_name="成功",
    )
    result_data = SafeTextField(
        null=True,
        blank=True,
        verbose_name="结果信息",
    )
    error_data = SafeTextField(
        null=True,
        blank=True,
        verbose_name="错误信息",
    )
    result_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="结果报告时间",
    )

    class Meta:
        abstract = True

    def clean_result(self, save=True):
        self.success = None
        self.result_data = None
        self.error_data = None
        self.result_time = None
        if save:
            self.save()

    def set_result(self, result, save=True):
        self.success = True
        self.result = result
        self.error = None
        self.result_time = timezone.now()
        if save:
            self.save()

    def set_error(self, error, save=True):
        self.success = False
        self.result = None
        self.error = BizError(error)
        self.result_time = timezone.now()
        if save:
            self.save()

    def _get_result(self):
        if not self.result_data:
            return None
        else:
            return json.loads(self.result_data)

    def _set_result(self, result):
        if result is None:
            self.result_data = None
        else:
            self.result_data = jsonutils.simple_json_dumps(result, ensure_ascii=False)

    result = property(_get_result, _set_result)

    def _get_error(self):
        if not self.error_data:
            return None
        else:
            return BizError(json.loads(self.error_data))

    def _set_error(self, error):
        if error is None:
            self.error_data = None
        else:
            self.error_data = jsonutils.simple_json_dumps(error, ensure_ascii=False)

    error = property(_get_error, _set_error)


class WithCountFields(models.Model):
    count = models.IntegerField(
        default=0,
        verbose_name="计数",
    )

    class Meta:
        abstract = True

    def incr(self, delta=1):
        """计数器加。"""
        from globallock.django import get_default_global_lock_manager

        lock_name = "WithCountFields:{}:{}:{}".format(
            self._meta.app_label,
            self._meta.model_name,
            self.pk,
        )
        lockman = get_default_global_lock_manager()
        with lockman.lock(lock_name) as lock:
            if lock.is_locked:
                self.count += delta
                self.save()
        return self.count

    def decr(self, delta=1):
        from globallock.django import get_default_global_lock_manager

        """计数器减。"""
        lock_name = "WithCountFields:{}:{}:{}".format(
            self._meta.app_label,
            self._meta.model_name,
            self.pk,
        )
        lockman = get_default_global_lock_manager()
        with lockman.lock(lock_name) as lock:
            if lock.is_locked:
                self.count -= delta
                self.save()
        return self.count


class WithExpireTimeFields(models.Model):

    EXPIRES_UNIT_SECOND = 10
    EXPIRES_UNIT_MINUTE = 20
    EXPIRES_UNIT_HOUR = 30
    EXPIRES_UNIT_DAY = 40
    EXPIRES_UNITS = [
        (EXPIRES_UNIT_SECOND, "秒"),
        (EXPIRES_UNIT_MINUTE, "分钟"),
        (EXPIRES_UNIT_HOUR, "小时"),
        (EXPIRES_UNIT_DAY, "天"),
    ]
    EXPIRES_SECONDS = {
        EXPIRES_UNIT_DAY: 60 * 60 * 24,
        EXPIRES_UNIT_HOUR: 60 * 60,
        EXPIRES_UNIT_MINUTE: 60,
        EXPIRES_UNIT_SECOND: 1,
    }

    expires = models.IntegerField(
        null=True,
        blank=True,
        verbose_name="过期时长",
    )
    expires_unit = models.IntegerField(
        choices=EXPIRES_UNITS,
        default=EXPIRES_UNIT_SECOND,
        verbose_name="过期时长单位",
    )
    expire_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="过期时间",
    )

    default_expires = None
    default_expires_unit = EXPIRES_UNIT_SECOND

    class Meta:
        abstract = True

    def clean_expire_time(self, save=True):
        self.expires = None
        self.expires_unit = None
        self.expire_time = None
        if save:
            self.save()

    def set_expire_time(self, expires=None, expires_unit=None, nowtime=None, save=True):
        if nowtime is None:
            nowtime = timezone.now()
        if expires is None:
            expires = self.default_expires
        if expires_unit is None:
            expires_unit = self.default_expires_unit
        self.expires = expires
        self.expires_unit = expires_unit
        self.expire_time = nowtime + datetime.timedelta(
            seconds=self.get_expire_seconds()
        )
        if save:
            self.save()

    def get_expire_seconds(self):
        multiple = self.EXPIRES_SECONDS.get(self.expires_unit, 1)
        return self.expires * multiple

    @property
    def is_expired(self):
        nowtime = timezone.now()
        if self.expire_time:
            if self.expire_time < nowtime:
                return True
        return False

    def save(self, *args, **kwargs):
        if self.expires is None:
            if self.default_expires:
                self.expires = self.default_expires
        if self.expires_unit is None:
            if self.default_expires_unit:
                self.expires_unit = self.default_expires_unit
        if self.expires:
            if self.expire_time is None:
                self.expire_time = timezone.now() + datetime.timedelta(
                    seconds=self.get_expire_seconds()
                )
        return super().save(*args, **kwargs)


class WithVisibleFields(models.Model):
    visible = models.BooleanField(
        null=True,
        verbose_name="是否显示",
    )
    hidden_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="隐藏时间",
    )
    visible_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="显示时间",
    )

    class Meta:
        permissions = [
            ("set_visible", "允许设置可见标记"),
            ("set_hidden", "允许设置隐藏标记"),
        ]
        abstract = True

    def save(self, *args, **kwargs):
        if self.visible:
            if self.hidden_time is not None:
                self.hidden_time = None
            if self.visible_time is None:
                self.visible_time = timezone.now()
        else:
            if self.hidden_time is None:
                self.hidden_time = timezone.now()
            if self.visible_time is not None:
                self.visible_time = None
        return super().save(*args, **kwargs)

    def set_hidden(self, save=True):
        self.visible = False
        if self.save:
            self.save()

    def set_visible(self, save=True):
        self.visible = True
        if self.save:
            self.save()

    def visible_display(self):
        return self.visible and "可见" or "隐藏"

    visible_display.short_description = "可见性"


class WithHotspotFields(models.Model):
    hotspot = models.BooleanField(
        null=True,
        verbose_name="是否热点",
    )
    hotspot_weight = models.IntegerField(
        null=True,
        blank=True,
        default=100,
        verbose_name="热度",
    )
    hotspot_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="设置热点时间",
    )
    non_hotspot_time = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="取消热点时间",
    )

    class Meta:
        permissions = [
            ("set_hotspot", "允许设置热点标记"),
            ("clean_hotspot", "允许清除热点标记"),
        ]
        abstract = True

    def save(self, *args, **kwargs):
        if self.hotspot:
            if self.hotspot_time is None:
                self.hotspot_time = timezone.now()
            if self.non_hotspot_time is not None:
                self.non_hotspot_time = None
        else:
            if self.hotspot_time is not None:
                self.hotspot_time = None
            if self.non_hotspot_time is None:
                self.non_hotspot_time = timezone.now()
        return super().save(*args, **kwargs)

    def set_hotspot(self, save=True):
        self.hotspot = True
        if save:
            self.save()

    def clear_hotspot(self, save=True):
        self.hotspot = False
        if save:
            self.save()

    def hotspot_display(self):
        return self.hotspot and "热点" or "非热点"

    hotspot_display.short_description = "热点状态"


class WithArgsKwargsFields(models.Model):
    args_raw = models.TextField(
        null=True,
        blank=True,
        verbose_name="args",
    )
    kwargs_raw = models.TextField(
        null=True,
        blank=True,
        verbose_name="kwargs",
    )

    def get_args(self):
        if not self.args_raw:
            return []
        else:
            return json.loads(self.args_raw)

    def set_args(self, args):
        self.args_raw = json.dumps(list(args))

    args = property(get_args, set_args)

    def get_kwargs(self):
        if not self.kwargs_raw:
            return {}
        else:
            return json.loads(self.kwargs_raw)

    def set_kwargs(self, kwargs):
        self.kwargs_raw = json.dumps(dict(kwargs))

    kwargs = property(get_kwargs, set_kwargs)

    class Meta:
        abstract = True
