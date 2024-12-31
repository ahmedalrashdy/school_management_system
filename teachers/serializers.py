from rest_framework import serializers

from teachers.models import Teacher

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'address', 'gender', 'email', 'phone', 'specialization', 'nationality', 
                  'religion', 'image') 
