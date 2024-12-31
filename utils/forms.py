from django import forms  
from .models import Religion, Nationality, Specialization  

class ReligionForm(forms.ModelForm):  
    class Meta:  
        model = Religion  
        fields = ['religion']  
        error_messages = {  
            'religion': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 30 حرف',  
            },  
        }  

class NationalityForm(forms.ModelForm):  
    class Meta:  
        model = Nationality  
        fields = ['nationality']  
        error_messages = {  
            'nationality': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 30 حرف',  
            },  
        }  

class SpecializationForm(forms.ModelForm):  
    class Meta:  
        model = Specialization  
        fields = ['specialization']  
        error_messages = {  
            'specialization': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 70 حرف',  
            },  
        }