from django import forms
from .models import *


# الفورم الخاص بالسنة الدراسية
class AcademicYearForm(forms.ModelForm):
    class Meta:
        model = AcademicYear
        fields = ['year', 'start_date', 'end_date', 'is_current', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # ترتيب الحقول بحيث تظهر من اليمين لليسار
        self.fields['year'].widget.attrs.update({'dir': 'rtl'})
        self.fields['start_date'].widget.attrs.update({'dir': 'ltr'})
        self.fields['end_date'].widget.attrs.update({'dir': 'ltr'})
        self.fields['description'].widget.attrs.update({'dir': 'rtl'})
        labels = {
            'year': 'السنة الأكاديمية',
            'start_date': 'تاريخ بداية السنة',
            'end_date': 'تاريخ نهاية السنة',
            'is_current': 'السنة الحالية',
            'description': 'وصف السنة',
        }
        error_messages = {
            'year': {
                'unique': 'السنة الأكاديمية موجودة بالفعل. يرجى اختيار سنة مختلفة.',
                'required': 'هذا الحقل مطلوب.',
                'max_length': 'عدد الأحرف المسموح به هو 9 فقط.',
            },
            'start_date': {
                'invalid': 'يرجى إدخال تاريخ صحيح بصيغة YYYY-MM-DD.',
            },
            'end_date': {
                'invalid': 'يرجى إدخال تاريخ صحيح بصيغة YYYY-MM-DD.',
            },
            'description': {
                'max_length': 'عدد الأحرف المسموح به في الوصف تجاوز الحد المسموح.',
            },
        }
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        # تحقق من أن تاريخ النهاية أكبر من تاريخ البداية
        if start_date and end_date and start_date >= end_date:
            raise forms.ValidationError(
                "تاريخ النهاية يجب أن يكون بعد تاريخ البداية."
            )
        return cleaned_data

#الفورم الخاص بتسجيل الشعبة
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['name', 'class_level', 'academic_year']
        labels = {
            'name': 'اسم الشعبة',
            'class_level': 'الصف الدراسي',
            'academic_year': 'السنة الأكاديمية',
        }
        error_messages = {
            'name': {
                'required': 'اسم الشعبة مطلوب.',
                'max_length': 'عدد الأحرف المسموح به في اسم الشعبة هو 50 فقط.',
            },
            'class_level': {
                'required': 'يجب اختيار الصف الدراسي.',
            },
            'academic_year': {
                'required': 'يجب اختيار السنة الأكاديمية.',
            },
            '__all__': {
                'unique_together': 'هذه الشعبة موجودة مسبقًا لنفس الصف الدراسي والسنة الأكاديمية.',
            },
        }
#الفورم الخاص بتسجيل الصف
class ClassLevelForm(forms.ModelForm):
    class Meta:
        model = ClassLevel
        fields = ['name', 'stage']
        labels = {
            'name': 'اسم الصف الدراسي',
            'stage': 'المستوى الدراسي',
        }
        error_messages = {
            'name': {
                'required': 'اسم الصف الدراسي مطلوب.',
                'unique': 'اسم الصف الدراسي موجود بالفعل. يرجى اختيار اسم مختلف.',
                'max_length': 'عدد الأحرف المسموح به في اسم الصف الدراسي هو 70 فقط.',
            },
            'stage': {
                'required': 'المستوى الدراسي مطلوب.',
                'invalid_choice': 'الخيار المحدد للمستوى الدراسي غير صالح.',
            },
        }
#الفورم الخاص بتسجيل مادة 
class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'class_level', 'semester', 'note']
        labels = {
            'name': 'اسم المادة الدراسية',
            'class_level': 'الصف',
            'semester': 'الفصل الدراسي',
            'note': 'ملاحظات',
        }
        error_messages = {
            'name': {
                'unique': 'اسم المادة الدراسية موجود بالفعل. يرجى اختيار اسم مختلف.',
                'required': 'هذا الحقل مطلوب.',
            },
            'class_level': {
                'required': 'يرجى اختيار الصف.',
            },
            'semester': {
                'required': 'يرجى اختيار الفصل الدراسي.',
            },
            'note': {
                'max_length': 'تجاوزت الملاحظات الحد المسموح للأحرف.',
            },
        }

    def clean(self):
        cleaned_data = super().clean()
        # تحقق من القيم الإضافية (إن وجدت) هنا
        return cleaned_data 
