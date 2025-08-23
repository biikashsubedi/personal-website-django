from django.db import models
from django.utils.translation import gettext_lazy as _

class Attendance(models.Model):
    HOURLY_RATE = 17.55

    STATUS_CHOICES = (
        ('checked_in', 'Checked In'),
        ('checked_out', 'Checked Out'),
    )

    name = models.CharField(_("Name"), max_length=200, default='Bikash Subedi')
    phone_number = models.CharField(_("Phone Number"), max_length=200, default='+14379846303')
    checkin_time = models.DateTimeField(_("Check-In Time"), blank=True, null=True)
    checkout_time = models.DateTimeField(_("Check-Out Time"), blank=True, null=True)
    status = models.CharField(_("Status"), max_length=20, choices=STATUS_CHOICES, default='checked_in')

    @property
    def hours_worked(self):
        if self.checkin_time and self.checkout_time:
            return (self.checkout_time - self.checkin_time).total_seconds() / 3600
        return 0

    @property
    def total_pay(self):
        return round(self.hours_worked * self.HOURLY_RATE, 2)

    def __str__(self):
        return self.name if self.name else ""

    class Meta:
        db_table = 'attendance_records'
        verbose_name_plural = 'Attendance Records'
