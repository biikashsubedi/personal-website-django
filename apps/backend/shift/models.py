from datetime import datetime, timedelta

from django.db import models
from django.utils.translation import gettext_lazy as _


class Shift(models.Model):
    WORKSPACE = (
        ('restaurant', 'Restaurant'),
    )

    SHIFT_TYPE = (
        ('regular', 'Regular Day'),
        ('holiday', 'Holiday'),
        ('overtime', 'Overtime'),
        ('doubletime', 'Double Time'),
    )

    name = models.CharField(_("Name"), max_length=200, default='Bikash Subedi')
    phone_number = models.CharField(_("Phone Number"), max_length=200, default='+14379846303')
    workspace = models.CharField(_("Work Space"), max_length=20, choices=WORKSPACE, default='restaurant')

    # Shift info
    date = models.DateField(_("Date"), default=datetime.now)
    checkin_time = models.TimeField(_("Check-In Time"), blank=True, null=True)
    checkout_time = models.TimeField(_("Check-Out Time"), blank=True, null=True)
    shift_type = models.CharField(_("Shift Type"), max_length=20, choices=SHIFT_TYPE, default='regular')

    # Pay rate
    hourly_rate = models.DecimalField(_("Hourly Rate"), max_digits=6, decimal_places=2, default=17.20)

    # Calculated fields
    hours_worked = models.DecimalField(_("Hours Worked"), max_digits=6, decimal_places=2, default=0)
    gross_income = models.DecimalField(_("Gross Income"), max_digits=10, decimal_places=2, default=0)
    cpp_deduction = models.DecimalField(_("CPP Deduction"), max_digits=10, decimal_places=2, default=0)
    ei_deduction = models.DecimalField(_("EI Deduction"), max_digits=10, decimal_places=2, default=0)
    tax_deduction = models.DecimalField(_("Tax Deduction"), max_digits=10, decimal_places=2, default=0)
    total_deductions = models.DecimalField(_("Total Deductions"), max_digits=10, decimal_places=2, default=0)
    net_income = models.DecimalField(_("Net Income"), max_digits=10, decimal_places=2, default=0)

    # Status
    status = models.BooleanField(_('Checked Out'), default=False)

    def save(self, *args, **kwargs):
        if self.checkin_time and self.checkout_time:
            checkin_dt = datetime.combine(self.date, self.checkin_time)
            checkout_dt = datetime.combine(self.date, self.checkout_time)
            if checkout_dt < checkin_dt:
                checkout_dt += timedelta(days=1)

            # Calculate worked hours
            self.hours_worked = round((checkout_dt - checkin_dt).total_seconds() / 3600, 2)

            # Determine multiplier
            multiplier = 1.0
            if self.shift_type == 'holiday':
                multiplier = 1.5
            elif self.shift_type == 'overtime':
                multiplier = 1.5
            elif self.shift_type == 'doubletime':
                multiplier = 2.0

            # Calculate gross income based on multiplier
            self.gross_income = round(self.hours_worked * float(self.hourly_rate) * multiplier, 2)

            # Auto deductions
            self.cpp_deduction = round(self.gross_income * 0.051, 2)  # 5.1%
            self.ei_deduction = round(self.gross_income * 0.016, 2)  # 1.6%
            self.tax_deduction = round(self.gross_income * 0.07, 2)  # 7% example tax
            self.total_deductions = (
                    self.cpp_deduction + self.ei_deduction + self.tax_deduction
            )

            # Net income
            self.net_income = round(self.gross_income - self.total_deductions, 2)
            self.status = True

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.date} ({self.shift_type})"

    class Meta:
        db_table = 'shifts'
        verbose_name_plural = 'Shifts'
