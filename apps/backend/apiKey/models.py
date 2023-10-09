from django.db import models
from django.utils.translation import gettext_lazy as _


class ApiKey(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    key = models.CharField(_("Key"), max_length=200, blank=True, null=True)
    hits = models.IntegerField(_("Hits"), default=0)
    status = models.BooleanField(_('Status'), default=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'api_keys'
        verbose_name_plural = 'Api Key'
