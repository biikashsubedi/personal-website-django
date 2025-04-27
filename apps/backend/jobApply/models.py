from django.db import models
from django.utils.translation import gettext_lazy as _

class JobApply(models.Model):
    STATUS_CHOICES = (
        ('not_applied', 'Not Applied'),
        ('applied', 'Applied'),
        ('got_response', 'Got Response'),
    )

    phone_number = models.CharField(_("Phone Number"), max_length=200, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=200, blank=True, null=True)
    full_address = models.TextField(_("Full Address"), blank=True, null=True)
    latitude = models.FloatField(_("Latitude"), blank=True, null=True)
    longitude = models.FloatField(_("Longitude"), blank=True, null=True)
    review_count = models.CharField(_("Review Count"), max_length=200, blank=True, null=True)
    rating = models.FloatField(_("Rating"), blank=True, null=True)
    timezone = models.CharField(_("Timezone"), max_length=100, blank=True, null=True)
    website = models.URLField(_("Website"), blank=True, null=True)
    place_id = models.CharField(_("Place ID"), max_length=255, blank=True, null=True)
    place_link = models.URLField(_("Place Link"), blank=True, null=True)
    types = models.TextField(_("Types"), blank=True, null=True)
    price_level = models.CharField(_("Price Level"), max_length=10, blank=True, null=True)
    sunday = models.CharField(_("Sunday Hours"), max_length=100, blank=True, null=True)
    monday = models.CharField(_("Monday Hours"), max_length=100, blank=True, null=True)
    tuesday = models.CharField(_("Tuesday Hours"), max_length=100, blank=True, null=True)
    wednesday = models.CharField(_("Wednesday Hours"), max_length=100, blank=True, null=True)
    thursday = models.CharField(_("Thursday Hours"), max_length=100, blank=True, null=True)
    friday = models.CharField(_("Friday Hours"), max_length=100, blank=True, null=True)
    saturday = models.CharField(_("Saturday Hours"), max_length=100, blank=True, null=True)
    city = models.CharField(_("City"), max_length=200, blank=True, null=True)
    state = models.CharField(_("State"), max_length=200, blank=True, null=True)
    verified = models.BooleanField(_("Verified"), default=False)
    photos = models.URLField(_("Photos Link"), blank=True, null=True)
    description = models.TextField(_("Description"), blank=True, null=True)
    sms = models.TextField(_("sms"), blank=True, null=True)
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    status = models.CharField(_("Status"), choices=STATUS_CHOICES, default='not_applied', max_length=20)

    def __str__(self):
        return self.name if self.name else ""

    class Meta:
        db_table = 'job_apply_lists'
        verbose_name_plural = 'Job Applies'
