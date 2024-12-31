from unfold.admin import ModelAdmin
from django.contrib import admin, messages
from .models import Teacher, TeacherSubject
from django.core.exceptions import ValidationError
from .forms import FormTeacherAdmin


# @admin.register(Teacher)
# class TeacherAdmin(UnfoldModelAdmin):
#     # exclude=('user',)
#     pass
    


# from django.contrib import admin
# from unfold.admin import ModelAdmin as UnfoldModelAdmin


# from .models import *

# @admin.register(Teacher)
# class TeacherAdmin(UnfoldModelAdmin):
#     # exclude=('user',)
#     pass
    



@admin.register(Teacher)
class TeacherAdmin(ModelAdmin):
    # form =FormTeacherAdmin
    exclude=('user',)
    list_display = ['name', 'gender', 'email', 'phone', 'specialization', 'nationality', 'religion',"image"]
    search_fields = ['name', 'email', 'phone']
    list_filter = ['gender', 'specialization', 'nationality', 'religion']

    def save_model(self, request, obj, form, change):
        try:
            obj.clean()  # التحقق من التكرار
            super().save_model(request, obj, form, change)
            if change:
                self.message_user(request, "تم تعديل بيانات المعلم بنجاح.", level=messages.SUCCESS)
            else:
                self.message_user(request, "تم حفظ بيانات المعلم بنجاح.", level=messages.SUCCESS)
        except ValidationError as e:
            self.message_user(request, ", ".join(e.messages), level=messages.ERROR)
@admin.register(TeacherSubject)
class TeacherSubjectAdmin(ModelAdmin):
    list_display = ['teacher', 'subject', 'section', 'academic_year']
    search_fields = ['teacher__name', 'subject__name', 'section__name']
    list_filter = ['academic_year', 'section', 'subject']


    
