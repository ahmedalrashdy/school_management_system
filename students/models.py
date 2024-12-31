from django.db import models
from school.models import AcademicYear, ClassLevel, Section
from users.models import Role, User
from utils.constants import   GENDER_CHOICES, RELATIONSHIP_CHOICES
from utils.funcs import upload_file
from utils.models import Nationality, Religion
from django.core.exceptions import ValidationError
from django.utils import timezone


class Student(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الطالب") 
    address = models.TextField(blank=True, null=True, verbose_name="عنوان الطالب")  
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, blank=True,default="male", verbose_name="نوع الطالب")
    place_of_birth = models.CharField(max_length=100, verbose_name="مكان الميلاد") 
    birth_date = models.DateField(verbose_name="تاريخ الميلاد") 
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف")
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الجنسية") 
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الديانة") 
    image = models.ImageField(upload_to=upload_file, blank=True, null=True, verbose_name="صورة الطالب")
    email = models.EmailField(unique=True,blank=True, null=True, verbose_name="البريد الإلكتروني")
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="student",null=True, verbose_name="المستخدم")
    
    
    def clean(self):
        super().clean()
        if self.email :
            if User.objects.filter(email=self.email,id=self.id).exists():
                raise ValidationError({"email": "البريد الإلكتروني موجود بالفعل"})
        return self.email
    
    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        
        if  not self.user  and self.email:
            student_role,created=Role.objects.get_or_create(id=Role.STUDENT)
            user = User.objects.create_user(email=self.email, password="complex12345")
            user.roles.add(student_role)
            self.user = user
        super(Student, self).save()
    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"

    def __str__(self):
        return self.name
        


class Attachment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")  
    file = models.FileField(upload_to=upload_file, verbose_name="ملف المرفق") 
    label = models.CharField(max_length=255, verbose_name="تسمية المرفق") 
    description = models.TextField(blank=True, null=True, verbose_name="وصف المرفق") 
    
    class Meta:
        verbose_name = "مرفق"
        verbose_name_plural = "المرفقات"
    def __str__(self):
        return self.label


class Guardian(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم ولي الأمر")
    image = models.ImageField(upload_to=upload_file, blank=True, null=True, verbose_name="صورة ولي الأمر")
    address = models.TextField(blank=True, null=True, verbose_name="عنوان ولي الأمر") 
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف") 
    email = models.EmailField(unique=True,blank=True, null=True, verbose_name="البريد الإلكتروني")   
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL,null=True, blank=True, verbose_name="الديانة")  
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL,null=True, blank=True, verbose_name="الجنسية")
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="guardian",null=True, verbose_name="المستخدم")
    
    
    def clean(self):
        super().clean()
        if self.email :
            if User.objects.filter(email=self.email,id=self.id).exists():
                raise ValidationError({"email": "البريد الإلكتروني موجود بالفعل"})
        return self.email
    
    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if  not self.user  and self.email:
            guardian_role,created=Role.objects.get_or_create(id=Role.GUARDIAN)
            user = User.objects.create_user(email=self.email, password="complex12345")
            user.roles.add(guardian_role)
            self.user = user
        super(Guardian, self).save()
            
    class Meta:
        verbose_name = "إدارة أولياء الأمور"
        verbose_name_plural = "إدارة أولياء الأمور"

    def __str__(self):
        return self.name

    
class StudentGuardian(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    guardian=models.ForeignKey(Guardian, on_delete=models.CASCADE, verbose_name="ولي الأمر")
    relationship=models.CharField(choices=RELATIONSHIP_CHOICES,max_length=15, verbose_name="صلة القرابة")
    class Meta:
        unique_together=("student","guardian")
        verbose_name="ولي الأمر"
        verbose_name_plural="أولياء الأمور"
        



class StudentAcademicRecord(models.Model):
    student=models.ForeignKey(Student,verbose_name="الطالب",on_delete=models.CASCADE)
    academic_year=models.ForeignKey(AcademicYear,verbose_name="السنة الأكادمية",on_delete=models.CASCADE)
    class_level=models.ForeignKey(ClassLevel,verbose_name="الصف",on_delete=models.CASCADE)
    is_verified=models.BooleanField(default=False,verbose_name="هل تم التأكيد")
    class Meta:
        unique_together=("student","academic_year","class_level")
        verbose_name="سجل دراسي"
        verbose_name_plural="سجلات دراسية"


class StudentSection(models.Model):
        student=models.ForeignKey(Student,verbose_name="الطالب",on_delete=models.CASCADE,related_name="student_section")
        section=models.ForeignKey(Section,verbose_name="الشعبة",on_delete=models.CASCADE,)
        academic_year=models.ForeignKey(AcademicYear, verbose_name="السنة الأكاديمية",on_delete=models.CASCADE)
        class Meta:
            unique_together = ("student","academic_year")
            verbose_name = "شعبة"
            verbose_name_plural = "الشعب"
