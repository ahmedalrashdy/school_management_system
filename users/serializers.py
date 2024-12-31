from rest_framework import serializers
from rest_framework.fields import MinLengthValidator

from students.serializers import GuardianSerializer, StudentSerializer
from teachers.serializers import TeacherSerializer
from .models import Role, User
from django.contrib.auth.password_validation import validate_password

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'id_display')

    id_display = serializers.CharField(source='get_id_display', read_only=True)

class UserSerializer(serializers.ModelSerializer):
    roles = RoleSerializer(many=True)
    teacher = TeacherSerializer(read_only=True)
    student = StudentSerializer(read_only=True)
    guardian = GuardianSerializer(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'name', 'roles', 'teacher', 'student', 'guardian')
        
        
    
    def get_teacher(self, obj):
        if hasattr(obj, 'teacher') and obj.teacher is not None:
            return TeacherSerializer(obj.teacher).data
        return None

    def get_student(self, obj):
        if hasattr(obj, 'student') and obj.student is not None:
            return StudentSerializer(obj.student).data
        return None

    def get_guardian(self, obj):
        if hasattr(obj, 'guardian') and obj.guardian is not None:
            return GuardianSerializer(obj.guardian).data
        return None



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, allow_blank=False, error_messages={
        'required': 'البريد الالكتروني مطلوب.',
                    'blank': 'لا يمكن ترك البريد الالكتروني فارغاً.',
                    "invalid": "الرجاء ادخال بريد لكتروني صحيحاً"
    })
    password = serializers.CharField(required=True, allow_blank=False, error_messages={
        'required': ' كلمة المرور مطلوب.',
                    'blank': 'لا يمكن ترك حقل تأكيد كلمة المرور فارغاً.',
    })
    
    

class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=100)
  


class ResetPasswordConfirmSerializer(serializers.Serializer):
    otp = serializers.CharField(max_length=6, error_messages={
        'required': 'OTP مطلوب.',
        'blank': 'لا يمكن ترك حقل OTP فارغاً.',
        'max_length': 'OTP يجب أن يكون 6 أرقام.'
    })
    token = serializers.CharField(required=True,
        error_messages={
        'required': 'الرمز مطلوب.',
        'blank': 'لا يمكن ترك حقل الرمز فارغاً.'
    })

    new_password = serializers.CharField(write_only=True, required=True, validators=[MinLengthValidator(8)], error_messages={
        'required': 'كلمة المرور الجديدة مطلوبة.',
        'blank': 'لا يمكن ترك حقل كلمة المرور الجديدة فارغاً.'
    })
    re_new_password = serializers.CharField(write_only=True, required=True, error_messages={
        'required': 'تأكيد كلمة المرور الجديدة مطلوب.',
        'blank': 'لا يمكن ترك حقل تأكيد كلمة المرور الجديدة فارغاً.'
    })

    def validate(self, attrs):
        if 'new_password' in attrs or 're_new_password' in attrs:
            if 'new_password' not in attrs:
                raise serializers.ValidationError({"new_password": "كلمة المرور الجديدة مطلوبة."})
            if 're_new_password' not in attrs:
                raise serializers.ValidationError({"re_new_password": "تأكيد كلمة المرور الجديدة مطلوب."})
            if attrs['new_password'] != attrs['re_new_password']:
                raise serializers.ValidationError({"re_new_password": "كلمتا المرور غير متطابقتين."})
        return attrs
    


