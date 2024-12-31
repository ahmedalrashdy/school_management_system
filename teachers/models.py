from django.db import models
from django.core.exceptions import ValidationError
from school.models import AcademicYear, Section, Subject
from users.models import Role, User
from utils.constants import  GENDER_CHOICES
from utils.funcs import upload_file
from utils.models import Nationality, Religion, Specialization
from django.db import models, transaction
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم المعلم")  
    address = models.CharField(max_length=150,blank=True, null=True, verbose_name="عنوان المعلم")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, default="male", verbose_name="نوع المعلم") 
    email = models.EmailField(unique=True,blank=True, null=True, verbose_name="البريد الإلكتروني")  
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="رقم الهاتف") 
    specialization = models.ForeignKey(Specialization, blank=True, null=True, verbose_name="التخصص",on_delete=models.SET_NULL)
    nationality = models.ForeignKey(Nationality, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الجنسية")
    religion = models.ForeignKey(Religion, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الديانة")
    image = models.ImageField(upload_to=upload_file, blank=True, null=True, verbose_name="صورة المعلم") 
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="teacher",null=True, verbose_name="المستخدم")
    
    def clean(self):
      super().clean()
      if self.email:
          if User.objects.filter(email=self.email,id=self.id).exists():
              raise ValidationError({"email": "البريد الإلكتروني موجود بالفعل"})
      return self.email
    
    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
        if  not self.user and self.email:
            teacher_role,created=Role.objects.get_or_create(id=Role.TEACHER)
            user = User.objects.create_user(email=self.email, password="complex12345")
            user.roles.add(teacher_role)
            self.user = user
        super(Teacher, self).save()

    
    
    class Meta:
      verbose_name = "معلم"
      verbose_name_plural = "المعلمين"
      
    def __str__(self):
      return self.name
  
  
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# @receiver(pre_save, sender=Teacher)
# def create_user_for_teacher(sender, instance, **kwargs):
#     if not instance.user:
#         user = User.objects.create_user(email=instance.email, password="complex12345")
#         instance.user = user
#         instance.save()
        
class TeacherSubject(models.Model):
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,verbose_name="المعلم")
    section=models.ForeignKey(Section,verbose_name="الشعبة",on_delete=models.CASCADE)
    academic_year=models.ForeignKey(AcademicYear, verbose_name="السنة الأكاديمية",on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name="المادة")
    class Meta:
      verbose_name = "مادة معلم"
      verbose_name_plural = "مواد المعلمين"   
      unique_together = ("teacher","subject","section","academic_year")
    