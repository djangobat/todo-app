import django_filters
from datetime import timedelta
import calendar

from django import forms
from django.utils.timezone import localtime, now

from .models import Topic, Task


def filter_created(queryset, name, value):
    no = localtime(now())
    middle_no = no.replace(hour=0, minute=0, second=0)
    if value == 'D':
        return queryset.filter(created__gte=middle_no, created__lte=no)
    elif value == 'W':
        monday_of_this_week = middle_no - timedelta(days=(middle_no.isocalendar()[2] - 1))
        monday_of_next_week = monday_of_this_week + timedelta(days=7)
        return queryset.filter(created__gte=monday_of_this_week, created__lt=monday_of_next_week)
    elif value == 'M':
        first_day = calendar.firstweekday()
        fist_weekday, number_of_days = calendar.monthrange(middle_no.year, middle_no.month)
        first_day_of_this_month = middle_no.replace(day=1)
        first_day_of_next_month = first_day_of_this_month + timedelta(days=number_of_days)
        return queryset.filter(created__gte=first_day_of_this_month, created__lt=first_day_of_next_month)
    
    return queryset


TIME_CHOICES = (
    ('D', 'Hôm nay'),
    ('W', 'Tuần này'),
    ('M', 'Tháng này'),
)

class TaskFilter(django_filters.FilterSet):
    created = django_filters.ChoiceFilter(choices=TIME_CHOICES, widget=forms.Select, method=filter_created, empty_label='Tất cả')

    class Meta:
        model = Task
        fields = ('topic', 'status', 'created', )
