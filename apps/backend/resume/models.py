from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Education(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    value = models.TextField(_("value"), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)
    details = models.JSONField(_("details"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'education'
        verbose_name_plural = 'Education'


class Experience(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    type = models.CharField(_("Type"), max_length=200, blank=True, null=True)
    value = models.TextField(_("value"), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)
    details = models.JSONField(_("details"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'experiences'
        verbose_name_plural = 'Experience'


class Skill(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    value = models.TextField(_("value"), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)
    details = models.JSONField(_("details"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'skills'
        verbose_name_plural = 'Skill'
