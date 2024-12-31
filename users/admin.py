from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import  Group

from users.forms import CustomUserChangeForm, CustomUserCreationForm
from .models import Role, User
from unfold.admin import ModelAdmin as UnfoldModelAdmin



admin.site.unregister(Group)
@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, UnfoldModelAdmin):
    pass




# @admin.register(User)
# class UserAdmin(UnfoldModelAdmin):
#     pass



@admin.register(User)
class CustomUserAdmin(BaseUserAdmin,UnfoldModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User

    list_display = ('email', 'name', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active', 'roles')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('name',)}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (('Roles'), {'fields': ('roles',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password', 'password2', 'is_active', 'is_staff', 'is_superuser', 'roles')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

    # def save_model(self, request, obj, form, change):
    #     # إذا كان المستخدم جديداً
    #     if not change:
    #         obj.set_password(form.cleaned_data["password1"])
    #     super().save_model(request, obj, form, change)


