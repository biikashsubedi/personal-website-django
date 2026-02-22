from datetime import date, timedelta
from decimal import Decimal

from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Sum
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .forms import ShiftForm
from .models import Shift


class Index(ListView):
    model = Shift
    template_name = "backend/shift/index.html"


class Create(SuccessMessageMixin, CreateView):
    model = Shift
    template_name = "backend/shift/form.html"
    form_class = ShiftForm
    success_message = "Shift Created Successfully."
    success_url = reverse_lazy('shift:index')


class Update(SuccessMessageMixin, UpdateView):
    model = Shift
    template_name = "backend/shift/form.html"
    form_class = ShiftForm
    success_message = "Shift Updated Successfully."
    success_url = reverse_lazy('shift:index')


class Delete(SuccessMessageMixin, DeleteView):
    model = Shift
    template_name = "backend/layouts/deletePopUp.html"
    success_message = "Shift Deleted Successfully."
    success_url = reverse_lazy('shift:index')


class SlipIndex(ListView):
    model = Shift
    template_name = "backend/shift/slip.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shifts = Shift.objects.all().order_by('date')  # oldest first

        if not shifts.exists():
            context['pay_periods'] = []
            return context

        # Use earliest shift date as anchor for biweekly periods
        first_shift_date = shifts.first().date
        start_date = date(2025, 9, 22)  # optional fixed anchor if you want
        if first_shift_date < start_date:
            start_date = first_shift_date

        # Create biweekly periods up to last shift
        last_shift_date = shifts.last().date
        periods = []
        while start_date <= last_shift_date:
            end_date = start_date + timedelta(days=14)
            periods.append((start_date, end_date))
            start_date = end_date + timedelta(days=1)  # next period starts after current ends

        # Group shifts by biweekly period
        pay_periods = []
        for s, e in periods:
            period_shifts = shifts.filter(date__gte=s, date__lte=e)
            if period_shifts.exists():
                total_hours = period_shifts.aggregate(hours=Sum('hours_worked'))['hours'] or 0
                total_gross = period_shifts.aggregate(gross=Sum('gross_income'))['gross'] or 0
                pay_periods.append({
                    'date_range': f"{s} - {e}",
                    'shifts': period_shifts,
                    'total_hours': round(total_hours, 2),
                    'total_gross': round(total_gross, 2),
                })

        context['pay_periods'] = pay_periods
        return context


def shift_detail_api(request, pk):
    try:
        shift = Shift.objects.get(pk=pk)

        # Define biweekly periods
        start_date = date(2025, 9, 22)  # example first pay period start
        periods = []
        while start_date <= date.today():
            end_date = start_date + timedelta(days=14)
            periods.append((start_date, end_date))
            start_date = end_date

        # Find the period this shift belongs to
        period = next(((s, e) for s, e in periods if s <= shift.date < e), None)
        if not period:
            return JsonResponse({'status': 'error', 'message': 'No pay period found'}, status=404)

        last_pay_date, next_pay_date = period

        # Get all shifts in this period for the same employee
        shifts = Shift.objects.filter(
            name=shift.name,
            date__gte=last_pay_date,
            date__lt=next_pay_date
        )

        total_hours = shifts.aggregate(hours=Sum('hours_worked'))['hours'] or 0
        total_gross = shifts.aggregate(gross=Sum('gross_income'))['gross'] or 0

        data = {
            'name': shift.name,
            'workspace': shift.workspace,
            'date_range': f"{last_pay_date} - {next_pay_date}",
            'hours_worked': round(total_hours, 2),
            'hourly_rate': shift.hourly_rate,
            'gross_income': round(total_gross, 2),
            'vacation_pay': (total_gross * Decimal('0.04')).quantize(Decimal('0.01')),
            'cpp_deduction': (total_gross * Decimal('0.0525')).quantize(Decimal('0.01')),
            'ei_deduction': (total_gross * Decimal('0.016')).quantize(Decimal('0.01')),
            'tax_deduction': (total_gross * Decimal('0.10')).quantize(Decimal('0.01')),
            'net_income': (total_gross - (
                    total_gross * Decimal('0.0525') + total_gross * Decimal('0.016') + total_gross * Decimal('0.10')
            )).quantize(Decimal('0.01'))
        }

        return JsonResponse({'status': 'success', 'data': data})

    except Shift.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Shift not found'}, status=404)
