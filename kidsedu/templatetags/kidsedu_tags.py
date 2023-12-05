from django import template
from kidsedu.models import *

register = template.Library()


@register.inclusion_tag('kidsedu/schedule.html')
def schedule_table():
    """Для таблицы расписания занятий."""
    table_times = ['08:00', '10:00', '12:00', '14:00', '16:00']
    qset = ScheduleEdu.objects.all().order_by('week_day').select_related('name_id')
    week_lst = [str(i) for i in range(1, 7)]
    return {
        'qset': qset,
        'week_lst': week_lst,
        'table_times': table_times,
    }


@register.inclusion_tag('kidsedu/classes.html')
def classes_progs():
    """Вывод трех программ занятий школы."""
    qset = ProgramEdu.objects.filter(pk__lte=3)
    classes_html = [
        'col-lg-4 col-md-6 col-12',
        'mt-5 mt-lg-0 mt-md-0 col-lg-4 col-md-6 col-12',
        'mt-5 mt-lg-0 col-lg-4 col-md-6 col-12',
    ]
    data_aos = 'fade-up'
    data_aos_delay = ['400', '500', '600']
    return {
        'qset': qset,
        'classes': classes_html,
        'data_aos': data_aos,
        'data_aos_delay': data_aos_delay,
    }


@register.inclusion_tag('kidsedu/add_form.html')
def add_person_form(form):
    """Отображает форму заявки."""
    return {'head_form_name': 'Форма заявки', 'form': form}


@register.inclusion_tag('kidsedu/feedback_form.html')
def feedback_form(form_fb):
    """Отображает форма обратной связи."""
    return {
        'head_form_name': 'Не стесняйтесь спрашивать что угодно',
        'form_fb': form_fb
        }
