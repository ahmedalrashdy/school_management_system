from tabnanny import verbose
from django.contrib.auth.models import BaseUserManager
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        user = self.create_user(email, password, **extra_fields)
        staff, created = Role.objects.get_or_create(id=Role.STAFF)
        superuser, created = Role.objects.get_or_create(id=Role.SUPERUSER)
        user.roles.add(staff)
        user.roles.add(superuser)
        return user


class Role(models.Model):
    STUDENT = 1
    TEACHER = 2
    SECRETARY = 3
    SUPERUSER = 4
    STAFF = 5
    GUARDIAN = 6
    ROLE_CHOICES = (
        (STUDENT, 'طالب'),
        (TEACHER, 'معلم'),
        (SECRETARY, 'سكرتير'),
        (SUPERUSER, 'مشرف عام'),
        (STAFF, 'موظف'),
        (GUARDIAN, 'ولي أمر'),
    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True, verbose_name="الدور")

    def __str__(self):
        return self.get_id_display()


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="الاسم الكامل"
    )
    email = models.EmailField("عنوان البريد الإلكتروني", unique=True)
    date_joined = models.DateTimeField(
        default=timezone.now, verbose_name="تاريخ الانضمام")
    roles = models.ManyToManyField(Role, verbose_name="الأدوار")
    is_staff = models.BooleanField(
        default=False, verbose_name="عضو فريق العمل")
    is_superuser = models.BooleanField(default=False, verbose_name="مشرف عام")
    is_active = models.BooleanField(default=True, verbose_name="نشط")
    has_reset_password = models.BooleanField(
        default=False, verbose_name="تغيير كلمة المرور")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    class Meta:
        verbose_name = "مستخدم"
        verbose_name_plural = "المستخدمين"

    @property
    def is_teacher(self):
        return self.roles.filter(id=Role.TEACHER).exists()

    def has_role(self, role_id):
        return self.roles.filter(id=role_id).exists()

    def __str__(self):
        return self.email
