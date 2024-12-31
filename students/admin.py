from django.contrib import admin  
from .models import *  
from unfold.admin import ModelAdmin
# استيراد InlineModelAdmin بدلاً من BaseModelAdmin  
from unfold.admin import TabularInline

# Inline model for attachments  
class StudentGuardianAdminInline(TabularInline):
    model=StudentGuardian
    extra=0
class AttachmentInline(TabularInline):  # تأكد من الوراثة من InlineModelAdmin  
    model = Attachment  
    extra = 0 # Number of empty forms to display  

@admin.register(Student)  
class StudentAdmin(ModelAdmin):  
    list_display = ('name', 'gender', 'place_of_birth', 'birth_date', 'phone', 'email')  
    search_fields = ('name', 'phone', 'email')  
    list_filter = ('gender', 'nationality', 'religion')  
    inlines = [StudentGuardianAdminInline,AttachmentInline]  # Add the inline for attachments  

@admin.register(Attachment)  
class AttachmentAdmin(ModelAdmin):  
    list_display = ('student', 'label', 'file')  
    search_fields = ('label',)  
    list_filter = ('student',)   

@admin.register(Guardian)  
class GuardianAdmin(ModelAdmin):  
    list_display = ('name', 'phone', 'email', 'nationality', 'religion')  
    search_fields = ('name', 'phone', 'email')  
    list_filter = ('nationality', 'religion')  

@admin.register(StudentGuardian)  
class StudentGuardianAdmin(ModelAdmin):  
    list_display = ('student', 'guardian', 'relationship')  
    search_fields = ('student__name', 'guardian__name')  
    list_filter = ('relationship',)  

@admin.register(StudentAcademicRecord)  
class StudentAcademicRecordAdmin(ModelAdmin): 
    list_display = ('student', 'academic_year', 'class_level', 'is_verified')  
    search_fields = ('student__name',)  
    list_filter = ('academic_year', 'class_level', 'is_verified')  

# @admin.register(StudentSection)  
# class StudentSectionAdmin(ModelAdmin):  
#     list_display = ('student', 'section', 'academic_year')  
#     search_fields = ('student__name',)  
#     list_filter = ('section', 'academic_year')  # إزالة القوس الزائد هناح

# from django.contrib import admin

# # Register your models here.

# from django.contrib import admin
# from unfold.admin import ModelAdmin as UnfoldModelAdmin


# from .models import *

# @admin.register(Student)
# class StudentAdmin(UnfoldModelAdmin):
#     exclude=('user',)
    

# @admin.register(Guardian)
# class GuardianAdmin(UnfoldModelAdmin):
#     exclude=('user',)
    
    
    
# @admin.register(StudentSection)
# class StudentSectionAdmin(UnfoldModelAdmin):
#     pass
    