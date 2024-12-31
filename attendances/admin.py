from django.contrib import admin
from .models import *
from .forms import *
from unfold.admin import ModelAdmin as UnfoldModelAdmin

from django.urls import path
from django.shortcuts import redirect
from . import views

@admin.register(Attendance)
class AttendanceAdmin(UnfoldModelAdmin):
    list_display = ['student', 'academic_day', 'status']
    search_fields = ['student__name', 'academic_day__date']
    list_filter = ['status','academic_day__date']
    # change_list_template = "attendance_preparation.html"
    change_form_template = "attendance_change_list.html"
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('prepare_attendance/', self.admin_site.admin_view(views.prepare_attendance), name='prepare_attendance'),
        ]
        return custom_urls + urls
@admin.register(AcademicDay)
class AcademicDayAdmin(UnfoldModelAdmin):
    form = AcademicDayForm
    list_display = ['date']
    search_fields = ['date']
