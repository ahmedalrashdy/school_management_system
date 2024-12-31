from django.db import models

from school.models import AcademicYear, ClassLevel
from students.models import Student
from utils.constants import FEES_TYPE_CHOICES

# Create your models here.
class StudyFees(models.Model):
    class_level=models.ForeignKey(ClassLevel,verbose_name='الفصل الدراسي',on_delete=models.CASCADE)
    academic_year=models.ForeignKey(AcademicYear,verbose_name='السنة الدراسية',on_delete=models.CASCADE)
    amount_due=models.FloatField(verbose_name="المبلغ المستحق")
    fees_type=models.CharField(max_length=20,choices=FEES_TYPE_CHOICES,verbose_name="نوع الرسوم")

    class Meta:
        unique_together = ("class_level", "academic_year", "fees_type")
        verbose_name = "رسوم دراسية"
        verbose_name_plural = "الرسوم الدراسية"
        
    def __str__(self):
        return f"{self.fees_type} for {self.class_level} in {self.academic_year}"
        


class Installment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    study_fees = models.ForeignKey(StudyFees, on_delete=models.CASCADE, verbose_name="الرسوم الدراسية")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="المبلغ المدفوع")
    payment_date = models.DateField(verbose_name="تاريخ الدفع")
    
    class Meta:
        verbose_name = "قسط"
        verbose_name_plural = "الأقساط"

    def __str__(self):
       return f"{self.student} paid {self.amount_paid} on {self.payment_date}"

