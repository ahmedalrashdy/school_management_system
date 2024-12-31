from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import *


@admin.register(Exam)
class ExamAdmin(ModelAdmin):
    list_display = ('name', 'subject', 'section', 'academic_year', 'date', 'max_value', 'passing_score')
    list_filter = ('academic_year', 'section', 'subject', 'date')
    search_fields = ('name', 'subject__name', 'section__name', 'academic_year__name')
    ordering = ('academic_year', 'section', 'subject', 'date')
    date_hierarchy = 'date'


from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import StudentResult, Exam


class SubjectFilter(admin.SimpleListFilter):
    title = _('المادة')  # عنوان الفلتر
    parameter_name = 'exam__subject'  # اسم المعلمة المستخدمة في URL

    def lookups(self, request, model_admin):
        subjects = set(Exam.objects.values_list('subject__id', 'subject__name'))
        return [(subject_id, subject_name) for subject_id, subject_name in subjects]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(exam__subject_id=self.value())
        return queryset


@admin.register(StudentResult)
class StudentResultAdmin(ModelAdmin):
    change_form_template = "admin/exams/attendance_form.html"
    list_display = ('student', 'exam', 'score')
    list_filter = ("exam__academic_year",SubjectFilter, "exam__section")  # استخدام الفلتر المخصص
    search_fields = ('student__name', 'exam__name', 'exam__subject__name', 'exam__section__name')
    ordering = ('exam__date', 'student')
