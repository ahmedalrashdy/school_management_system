from dataclasses import fields
from rest_framework import serializers

from school.models import AcademicYear, ClassLevel

from rest_framework import serializers
from school.models import Section

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'name', 'academic_year']

class ClassLevelSerializer(serializers.ModelSerializer):
    section = serializers.SerializerMethodField()

    class Meta:
        model = ClassLevel
        fields = "__all__"


    
    def get_section(self, obj):
        current_year =AcademicYear.get_current_year()  
        if not current_year:
            raise ValueError("يجب تحديد السنة الحالية في الـ context")
        
        sections = Section.objects.filter(class_level=obj, academic_year=current_year)
        return SectionSerializer(sections, many=True).data