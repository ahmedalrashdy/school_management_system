from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from utils.constants import RELATIONSHIP_CHOICES
class Religion(models.Model):
    religion= models.CharField(max_length=30, verbose_name='الدين')

    class Meta:
        verbose_name = 'ديانة'
        verbose_name_plural = 'الديانات'
    def __str__(self):
        return self.religion

class Nationality(models.Model):
    nationality = models.CharField(max_length=30,verbose_name='الجنسية')

    class Meta:
        verbose_name = 'جنسية'
        verbose_name_plural = 'جنسيات'
    def __str__(self):
        return self.nationality


class Specialization(models.Model):
    specialization = models.CharField(max_length=70, verbose_name='التخصص')
    class Meta:
        verbose_name = 'تخصص'
        verbose_name_plural = 'تخصصات'
    def __str__(self):
        return self.specialization
#  from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
# class Religion(models.Model):
#     religion= models.CharField(max_length=30, verbose_name='الدين')

#     class Meta:
#         verbose_name = 'ديانة'
#         verbose_name_plural = 'الديانات'

# class Nationality(models.Model):
#     nationality = models.CharField(max_length=30, verbose_name='الجنسية')
#     class Meta:
#         verbose_name = 'جنسية'
#         verbose_name_plural = 'جنسيات'

# class Specialization(models.Model):
#     specialization = models.CharField(max_length=70, verbose_name='التخصص')
#     class Meta:
#         verbose_name = 'تخصص'
#         verbose_name_plural = 'تخصصات'
