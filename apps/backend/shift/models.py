from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timedelta

class Shift(models.Model):
    HOURLY_RATE = 17.55

    STATUS_CHOICES = (
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    )
    WORKSPACE = (
        ('bhai', 'Bhai'),
        ('miniso', 'Miniso'),
    )

    name = models.CharField(_("Name"), max_length=200, default='Bikash Subedi')
    phone_number = models.CharField(_("Phone Number"), max_length=200, default='+14379846303')
    date = models.DateField(_("Date"), auto_now_add=True)
    checkin_time = models.TimeField(_("Check-In Time"), blank=True, null=True)
    checkout_time = models.TimeField(_("Check-Out Time"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES, default='checked_in')
    workspace = models.CharField(_("Work Space"), max_length=20, choices=WORKSPACE, default='miniso')


    @property
    def hours_worked(self):
        if self.checkin_time and self.checkout_time:
            checkin_dt = datetime.combine(self.date, self.checkin_time)
            checkout_dt = datetime.combine(self.date, self.checkout_time)

            if checkout_dt < checkin_dt:
                checkout_dt += timedelta(days=1)

            return round((checkout_dt - checkin_dt).total_seconds() / 3600, 2)
        return 0

    @property
    def total_pay(self):
        return round(self.hours_worked * self.HOURLY_RATE, 2)

    def __str__(self):
        return self.name if self.name else ""

    class Meta:
        db_table = 'shift_records'
        verbose_name_plural = 'Shift Records'
