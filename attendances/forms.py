from django import forms
from .models import *
from school.models import *
from utils.constants import ATTENDANCE_CHOICES

#////////////////////////////////////////////////////////
class AttendancePreparationForm(forms.Form):
    academic_year = forms.ModelChoiceField(
        queryset=AcademicYear.objects.all(),
        label="السنة الأكاديمية",
        empty_label="اختر السنة الأكاديمية",
    )
    class_ = forms.ModelChoiceField(
        queryset=ClassLevel.objects.none(),  # يتم تحديثها ديناميكيًا
        label="الفصل",
        empty_label="اختر الفصل",
    )
    section = forms.ModelChoiceField(
        queryset=Section.objects.none(),  # يتم تحديثها ديناميكيًا
        label="الشعبة",
        empty_label="اختر الشعبة",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['academic_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['class_'].widget.attrs.update({'class': 'form-control'})
        self.fields['section'].widget.attrs.update({'class': 'form-control'})

#////////////////////////////////////////////////////////
class AcademicDayForm(forms.ModelForm):
    class Meta:
        model = AcademicDay
        fields = ['date']

    # تخصيص رسائل الخطأ باللغة العربيةf
    error_messages = {
        'date': {
            'required':('يرجى اختيار التاريخ.'),
            'invalid': ('التاريخ الذي أدخلته غير صالح.'),
        },
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # تخصيص الحقول لتدعم الترجمة بشكل أفضل
        for field in self.fields.values():
            field.widget.attrs.update({'dir': 'rtl'})