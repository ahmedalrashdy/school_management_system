from django.db import models

from school.models import AcademicYear, Section, Subject
from students.models import Student


class Exam(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الامتحان")
    min_value = models.DecimalField(default=0, verbose_name="الحد الأدنى للعلامة" ,max_digits=4, decimal_places=2)
    max_value = models.DecimalField(default=50,verbose_name="الحد الأقصى للعلامة", max_digits=4, decimal_places=2)
    passing_score = models.DecimalField(default=25, verbose_name="علامة النجاح", max_digits=4, decimal_places=2)
    subject=models.ForeignKey(Subject,verbose_name="المادة ",on_delete=models.CASCADE)
    section=models.ForeignKey(Section,on_delete=models.CASCADE,verbose_name="الشعبة")
    academic_year=models.ForeignKey(AcademicYear,on_delete=models.CASCADE,verbose_name="السنة الدراسية")
    date=models.DateField(verbose_name="تاريخ الامتحان")

    class Meta:
        verbose_name = "امتحان"
        verbose_name_plural = "الامتحانات"
        unique_together = ("name","subject","section","academic_year")
        

    def __str__(self):
        return f"{self.name} {self.section}"
    

class StudentResult(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,verbose_name="الطالب")
    exam=models.ForeignKey(Exam,on_delete=models.CASCADE,verbose_name="الامتحان")
    score=models.DecimalField(verbose_name="الدرجة", max_digits=4, decimal_places=2)
    
    class Meta:
        verbose_name ="نتائج الامتحان"
        verbose_name_plural = "نتائج الامتحان"
        unique_together = ("student","exam")
        
        