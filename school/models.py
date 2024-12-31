from django.db import models
from utils.constants import  SEMESTER_CHOICES, STAGE_CHOICES

class ClassLevel(models.Model):
    name = models.CharField(max_length=70, unique=True, verbose_name="اسم الصف الدراسي")
    stage= models.CharField(max_length=50,choices=STAGE_CHOICES, verbose_name="المستوى الدراسي")
    class Meta:
        verbose_name = "صف دراسي"
        verbose_name_plural = "الصفوف الدراسية"

    def __str__(self):
        return self.name
    
class AcademicYear(models.Model):
    year = models.CharField(max_length=9,unique=True, verbose_name="السنة الأكاديمية") 
    start_date = models.DateField(verbose_name="تاريخ بداية السنة",null=True,blank=True) 
    end_date = models.DateField(verbose_name="تاريخ نهاية السنة",null=True,blank=True) 
    is_current = models.BooleanField(default=False, verbose_name="السنة الحالية")
    description = models.TextField(blank=True, null=True, verbose_name="وصف السنة")  
    
    
    
    @staticmethod
    def get_current_year():
        return AcademicYear.objects.filter(is_current=True).first()
    class Meta:
        verbose_name = "سنة أكاديمية"
        verbose_name_plural = "السنوات الأكاديمية"
        
    def __str__(self):
        return f"{self.year}"
    



        
class Subject(models.Model):
    name = models.CharField(max_length=50,verbose_name="اسم المادة الدراسية")
    class_level=models.ForeignKey(ClassLevel,on_delete=models.CASCADE,verbose_name="الصف")
    semester=models.CharField(max_length=50,choices=SEMESTER_CHOICES,verbose_name="الفصل الدراسي")
    note = models.TextField(blank=True, null=True, verbose_name="ملاحظات")

    class Meta:
        verbose_name = "مادة دراسية"
        verbose_name_plural = "المواد الدراسية"
        unique_together = ("name","class_level","semester")

    def __str__(self):
      return f"{self.name} {self.class_level} {self.semester}"


class Section(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم الشعبة")
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE, verbose_name="الصف الدراسي")
    academic_year=models.ForeignKey(AcademicYear, verbose_name="السنة الأكاديمية",on_delete=models.CASCADE)
    class Meta:
      verbose_name = "شعبة"
      verbose_name_plural = "الشعب"
      unique_together = ("name","class_level","academic_year")

    def __str__(self):
      return f"{self.name} - {self.class_level} - {self.academic_year}"






        

    

