from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(_("name"), max_length=200, blank=True, null=True)
    email = models.CharField(_("email"), max_length=200, blank=True, null=True)
    phone = models.CharField(_("phone"), max_length=200, blank=True, null=True)
    message = models.TextField(_("message"), blank=True, null=True)
    details = models.JSONField(_("details"), blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'contact_us'
        verbose_name_plural = 'Contact Us'
