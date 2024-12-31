from django import forms
    
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

from .models import User, Role


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='البريد الإلكتروني',
        widget=forms.EmailInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all pr-10'
        }),
        error_messages={
            'required': 'يرجى إدخال البريد الإلكتروني.',
            'invalid': 'يرجى إدخال بريد إلكتروني صالح.'
        }
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all pr-10'
        }),
        label='كلمة المرور',
        error_messages={
            'required': 'يرجى إدخال كلمة المرور.'
        }
    )

from django import forms
from django.contrib.auth.forms import UserChangeForm

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='كلمة المرور',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all pr-10'
        }),
        error_messages={
            'required': 'يرجى إدخال كلمة المرور.'
        }
    )
    password2 = forms.CharField(
        label='تأكيد كلمة المرور',
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'w-full px-4 py-3 rounded-lg border border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all pr-10'
        }),
        error_messages={
            'required': 'يرجى تأكيد كلمة المرور.'
        }
    )

    class Meta:
        model = User
        fields = ('email', 'name')
        error_messages = {
            'email': {
                'required': 'يرجى إدخال البريد الإلكتروني.',
                'invalid': 'يرجى إدخال بريد إلكتروني صالح.'
            },
            'name': {
                'required': 'يرجى إدخال الاسم.'
            }
        }

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("كلمتا المرور غير متطابقتين.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'password', 'is_active', 'is_staff', 'roles')
        error_messages = {
            'email': {
                'required': 'يرجى إدخال البريد الإلكتروني.',
                'invalid': 'يرجى إدخال بريد إلكتروني صالح.'
            },
            'name': {
                'required': 'يرجى إدخال الاسم.'
            },
            'password': {
                'required': 'يرجى إدخال كلمة المرور.'
            }
        }


