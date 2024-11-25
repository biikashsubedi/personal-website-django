from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Education(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    year = models.CharField(_("year"), max_length=200, blank=True, null=True)
    location = models.CharField(_("location"), max_length=200, blank=True, null=True)
    background = models.CharField(_("background"), max_length=200, blank=True, null=True)
    value = models.TextField(_("value"), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)
    details = models.JSONField(_("details"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'educations'
        verbose_name_plural = 'Education'


class Experience(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    type = models.CharField(_("Type"), max_length=200, blank=True, null=True)
    year = models.CharField(_("year"), max_length=200, blank=True, null=True)
    location = models.CharField(_("location"), max_length=200, blank=True, null=True)
    company = models.CharField(_("company"), max_length=200, blank=True, null=True)
    background = models.CharField(_("background"), max_length=200, blank=True, null=True)
    value = RichTextField(blank=True, null=True)
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
    icon = models.TextField(_("icon"), blank=True, null=True)
    background = models.TextField(_("background"), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)
    details = models.JSONField(_("details"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'skills'
        verbose_name_plural = 'Skill'


class KeySkill(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'key_skills'
        verbose_name_plural = 'Key Skills'


class Project(models.Model):
    label = models.CharField(_("label"), max_length=200, blank=True, null=True)
    url = models.CharField(_("url"), max_length=200, blank=True, null=True)
    icon = models.ImageField(_('icon'), default='default/image.png', upload_to='projects')
    background = models.TextField(_("background"), blank=True, null=True)
    status = models.BooleanField(_('status'), default=True)
    position = models.IntegerField(_("position"), blank=True, null=True)

    def __str__(self):
        return self.label

    class Meta:
        db_table = 'projects'
        verbose_name_plural = 'Project'
