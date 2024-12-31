from django import forms
    
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import Teacher


class FormTeacherAdmin(forms.Form):
    list_display = ['name', 'gender', 'email', 'phone', 'specialization', 'nationality', 'religion',"image"]
    search_fields = ['name', 'email', 'phone']
    list_filter = ['gender', 'specialization', 'nationality', 'religion']

    class Meta:
        model =Teacher
        fields = ('name', 'gender', 'email', 'phone', 'specialization', 'nationality', 'religion',"image")
        error_messages={
            # 'name': {
            #     'required': 'يرجى إدخال اسم المعلم.',
            #     'invalid': 'يرجى إدخال بريد إلكتروني صالح.'
            # },
            'name': {
                'required': 'يرجى إدخال الاسم.'
            },
            # 'password': {
            #     'required': 'يرجى إدخال كلمة المرور.'
            # }
        }
        