
from rest_framework import serializers
from .models import  Student, Guardian



class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'name', 'address', 'gender', 'place_of_birth', 'birth_date', 'phone', 'nationality', 'religion', 'image', 'email')  

class GuardianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guardian
        fields = ('id', 'name', 'image', 'address', 'phone', 'email', 'religion', 'nationality')



