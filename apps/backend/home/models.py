from django.db import models
from django.utils.translation import gettext_lazy as _


class Config(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    type = models.CharField(_("type"), max_length=200, blank=True, null=True)
    value = models.TextField(_("value"), blank=True, null=True)
    detail = models.JSONField(_("detail"), blank=True, null=True)
    status = models.BooleanField(_('Status'), default=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'configs'
        verbose_name_plural = 'Config'


class Link(models.Model):
    label = models.CharField(_("label"), max_length=200)
    url = models.CharField(_("url"), max_length=200)
    icon = models.CharField(_("icon"), max_length=200)
    status = models.BooleanField(_('Status'), default=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'links'
        verbose_name_plural = 'Link'
