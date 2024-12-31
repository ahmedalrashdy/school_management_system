from django.contrib import admin

# Register your models here.
from django.contrib import admin  
from .models import Religion, Nationality, Specialization 
from unfold.admin import ModelAdmin 
from unfold.admin import TabularInline

# Inline model for attachments  
class ReligionAdmin(TabularInline):
    model=Religion
    extra=1
class NationalityAdmin(TabularInline):  
    model = Nationality
    extra = 1  # Number of empty forms to display  
class SpecializationAdmin(TabularInline):  # تأكد من الوراثة من InlineModelAdmin  
    model = Specialization
    extra = 1  

@admin.register(Religion)  
class ReligionAdmin(ModelAdmin):  
    list_display = ('religion',)  
    search_fields = ('religion',)  
    list_filter = ('religion',)  

@admin.register(Nationality)  
class NationalityAdmin(ModelAdmin):  
    list_display = ('nationality',)  
    search_fields = ('nationality',)  
    list_filter = ('nationality',)  

@admin.register(Specialization)  
class SpecializationAdmin(ModelAdmin):  
    list_display = ('specialization',)  
    search_fields = ('specialization',)  
    list_filter = ('specialization',)