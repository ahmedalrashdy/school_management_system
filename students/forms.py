from django import forms  
from .models import *  

class StudentForm(forms.ModelForm):  
    class Meta:  
        model = Student  
        fields = ['name', 'address', 'gender', 'place_of_birth', 'birth_date', 'phone', 'nationality', 'religion', 'image', 'email']  
        error_messages = {  
            'name': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 80 حرف',  
            },  
            'phone': {  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 15 حرف',  
            },  
            'email': {  
                'invalid': 'البريد الإلكتروني غير صالح',  
            },  
        }  

class AttachmentForm(forms.ModelForm):  
    class Meta:  
        model = Attachment  
        fields = ['student', 'file', 'label', 'description']  
        error_messages = {  
            'label': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 80 حرف',  
            },  
            'file': {  
                'required': 'يجب تحميل ملف',  
            },  
        }  

class GuardianForm(forms.ModelForm):  
    class Meta:  
        model = Guardian  
        fields = ['name', 'image', 'address', 'phone', 'email', 'religion', 'nationality']  
        error_messages = {  
            'name': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 80 حرف',  
            },  
            'phone': {  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 20 حرف',  
            },  
            'email': {  
                'invalid': 'البريد الإلكتروني غير صالح',  
            },  
        }  

class StudentGuardianForm(forms.ModelForm):  
    class Meta:  
        model = StudentGuardian  
        fields = ['student', 'guardian', 'relationship']  
        error_messages = {  
            'relationship': {  
                'required': 'مدا الحقول المطلوبة',  
                'max_length': 'الحد الأقصى لطول هذا الحقل هو 15 حرف',  
            },  
        }  

class StudentAcademicRecordForm(forms.ModelForm):  
    class Meta:  
        model = StudentAcademicRecord  
        fields = ['student', 'academic_year', 'class_level', 'is_verified']  
        error_messages = {  
            'student': {  
                'required': 'هذا الحقول المطلوبة',  
            },  
            'academic_year': {  
                'required': 'هذا الحقول المطلوبة',  
            },  
            'class_level': {  
                'required': 'هذا الحقول المطلوبة',  
            },  
        }  

# class StudentSectionForm(forms.ModelForm):  
#     class Meta:  
#         model = StudentSection  
#         fields = ['student', 'section', 'academic_year']  
#         error_messages = {  
#             'student': {  
#                     'required': 'مدا الحقول المطلوبة',  
#             },  
#             'section': {  
#                 'required': 'مدا الحقول المطلوبة',  
#             },  
#             'academic_year': {  
#                 'required': 'مدا الحقول المطلوبة',  
#             },  
#         }