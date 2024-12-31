from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from students.models import Student
from utils.constants import ATTENDANCE_CHOICES
from school.models import Section

# Create your models here.
class AcademicDay(models.Model):
    date = models.DateField(verbose_name=("التاريخ"))

    class Meta:
        verbose_name =("اليوم الأكاديمي")
        verbose_name_plural =("الأيام الأكاديمية")

    def __str__(self):
        return str(self.date)
def get_default_section():
    try:
        return Section.objects.first() 
    except ObjectDoesNotExist:
        return None  
    
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    academic_day = models.ForeignKey(AcademicDay, on_delete=models.CASCADE, verbose_name="اليوم الأكاديمي")
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name="الشعبة",default=get_default_section)
    status = models.CharField(max_length=10,choices=ATTENDANCE_CHOICES,verbose_name="حالة الحضور")

    class Meta:
        unique_together = ("student", "academic_day","section")
        verbose_name = "تحضير"
        verbose_name_plural = "تحضير"
    def __str__(self):
        return f"{self.student} {self.status} in {self.academic_day}"