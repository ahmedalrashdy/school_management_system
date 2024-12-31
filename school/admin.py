
from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from .models import *
from .forms import *
from django.urls import reverse
from django.shortcuts import redirect,render
from django.http import HttpResponseRedirect




@admin.register(AcademicYear)
class AcademicYearAdmin(UnfoldModelAdmin):
    form=AcademicYearForm
    list_filter = ['is_current', 'start_date', 'end_date']  
    search_fields = ['year', 'description'] 


@admin.register(ClassLevel)
class ClassLevelAdmin(UnfoldModelAdmin):
    # استخدام الفورم المخصص
    form = ClassLevelForm
    # حقول البحث
    search_fields = ['name', 'stage']
    # الفلاتر الجانبية
    list_filter = ['stage']
    # الحقول المعروضة في القائمة الرئيسية
    list_display = ['name', 'stage']
    # تخصيص الرسائل عند الحفظ
    # تخصيص الرسالة عند الحفظ
    def save_model(self, request, obj, form, change):
        if change:  # إذا كانت عملية تعديل
            obj.save()
            self.message_user(request, "نجحت عملية التعديل بنجاح.", level="success")
        else:  # إذا كانت عملية إضافة
            obj.save()
            self.message_user(request, "تمت عملية الإضافة بنجاح.", level="success")
    # def save_model(self, request, obj, form, change):
    #     try:
    #         super().save_model(request, obj, form, change)
    #     except Exception as e:
    #         form.add_error(None, f"حدث خطأ أثناء الحفظ: {str(e)}")

# إجراء للتوجيه إلى صفحة التعديل
def edit_record_action(modeladmin, request, queryset):
    if queryset.count() == 1:  # تأكد من اختيار سجل واحد فقط
        obj = queryset.first()
        # توليد رابط صفحة التعديل
        edit_url = reverse(f'admin:{obj._meta.app_label}_{obj._meta.model_name}_change', args=[obj.id])
        return HttpResponseRedirect(edit_url)
    else:
        modeladmin.message_user(request, "يرجى تحديد سجل واحد فقط للتعديل.", level="error")

edit_record_action.short_description = "تعديل السجل المحدد"  # نص الإجراء

@admin.register(Section)
class SectionAdmin(UnfoldModelAdmin):
    form = SectionForm
    
    # تحديد الحقول القابلة للبحث
    search_fields = ['name', 'academic_year__year']
    
    # إضافة فلاتر جانبية
    list_filter = ['class_level', 'academic_year']
    
    # عرض الحقول في القائمة الرئيسية
    list_display = ['name', 'class_level', 'academic_year']
    actions = [edit_record_action,]
    # تخصيص الرسائل عند الحفظ
    def save_model(self, request, obj, form, change):
        try:
            super().save_model(request, obj, form, change)
        except Exception as e:
            form.add_error(None, f"حدث خطأ أثناء الحفظ: {str(e)}")

@admin.register(Subject)
class SubjectAdmin(UnfoldModelAdmin):
    form = SubjectForm
    list_display = ['name', 'class_level', 'semester']
    list_filter = ['class_level', 'semester']
    search_fields = ['name', 'class_level__name', 'semester']
    def save_model(self, request, obj, form, change):
        if change:  # إذا كان تعديل
            obj.save()
            self.message_user(request, "تمت عملية التعديل بنجاح.", level="success")
        else:  # إذا كان إضافة
            obj.save()
            self.message_user(request, "تمت عملية الإضافة بنجاح.", level="success")

    def delete_model(self, request, obj):
        obj.delete()
        self.message_user(request, "تمت عملية الحذف بنجاح.", level="success")