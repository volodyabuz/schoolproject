from django.contrib import admin
from .models import *

class ProgramEduAdmin(admin.ModelAdmin):
    list_display = ('name', 'min_age', 'max_age', 'about', 'photo', 'price')
    prepopulated_fields = {'slug': ('name',)}

class ScheduleEduAdmin(admin.ModelAdmin):
    list_display = ('name_id', 'week_day', 'start_edu', 'finish_edu')

admin.site.register(ProgramEdu, ProgramEduAdmin)
admin.site.register(ScheduleEdu, ScheduleEduAdmin)
admin.site.register(PersonForm)
