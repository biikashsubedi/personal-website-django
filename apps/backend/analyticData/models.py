from django.db import models
from django.utils.translation import gettext_lazy as _


class IPAnalytic(models.Model):
    api = models.CharField(_('Api Name'), max_length=200, blank=True, null=True)
    ip_address = models.CharField(_('IP Address'), max_length=200, blank=True, null=True)
    hits = models.IntegerField(_('Hits'), blank=True, null=True)
    city = models.CharField(_('City'), max_length=200, blank=True, null=True)
    region = models.CharField(_('Region'), max_length=200, blank=True, null=True)
    country = models.CharField(_('Country'), max_length=200, blank=True, null=True)
    country_code = models.CharField(_('Country Code'), max_length=200, blank=True, null=True)
    latitude = models.CharField(_('Latitude'), max_length=200, blank=True, null=True)
    longitude = models.CharField(_('Longitude'), max_length=200, blank=True, null=True)
    internet_provider = models.CharField(_('Internet Provider'), max_length=200, blank=True, null=True)
    timezone = models.CharField(_('Timezone'), max_length=200, blank=True, null=True)
    location_accuracy = models.CharField(_('Location Accuracy'), max_length=200, blank=True, null=True)
    last_hit_at = models.DateTimeField(_('Last Hit At'), blank=True, null=True)
    completed = models.BooleanField(_('Completed'), default=False)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return self.ip_address

    class Meta:
        db_table = 'analytics_ip'
        verbose_name_plural = 'IP Analytic'


class DeviceAnalytic(models.Model):
    user_agent = models.CharField(_('User Agent'), max_length=200, blank=True, null=True)
    device = models.CharField(_('Device Name'), max_length=200, blank=True, null=True)
    browser_version = models.CharField(_('Browser version'), max_length=200, blank=True, null=True)
    os = models.CharField(_('OS'), max_length=200, blank=True, null=True)
    os_version = models.CharField(_('OS Version'), max_length=200, blank=True, null=True)
    browser = models.CharField(_('Browser'), max_length=200, blank=True, null=True)
    hits = models.IntegerField(_('Hits'), blank=True, null=True)
    last_hit_at = models.DateTimeField(_('Last Hit At'), blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)

    def __str__(self):
        return self.device

    class Meta:
        db_table = 'analytics_web_device'
        verbose_name_plural = 'Web Device Analytic'
