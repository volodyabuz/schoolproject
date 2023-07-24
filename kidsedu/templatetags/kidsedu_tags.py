from django import template
from kidsedu.models import *

register = template.Library()

@register.inclusion_tag('kidsedu/schedule.html')
def schedule_table():
    table_times = ['08:00', '10:00', '12:00', '14:00', '16:00']
    qset = ScheduleEdu.objects.all().order_by('week_day')
    week_lst = [str(i) for i in range(1, 7)]
    return {
        'qset': qset,
        'week_lst': week_lst,
        'table_times': table_times,
    }
