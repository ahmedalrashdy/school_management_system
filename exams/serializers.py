from rest_framework import serializers
from .models import  Exam
from school.models import Section

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'name', 'min_value', 'max_value', 'passing_score', 'date', 'subject']


class SectionSerializer(serializers.ModelSerializer):
    exams = serializers.SerializerMethodField()

    class Meta:
        model = Section
        fields = ['id', 'name', 'class_level', 'academic_year', 'exams']

    def get_exams(self, obj):
        exams = Exam.objects.filter(section=obj)
        return ExamSerializer(exams, many=True).data



from rest_framework import serializers
from .models import Exam, StudentResult, Student


class StudentResultInputSerializer(serializers.Serializer):
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), required=True)
    result = serializers.DictField(
        child=serializers.DecimalField(max_digits=4, decimal_places=2),
        required=True
    )

    def validate(self, data):
        exam = data.get("exam")
        result = data.get("result")
        
        # تحقق من أن الطلاب الموجودين في result ينتمون إلى نفس الشعبة
        students = Student.objects.filter(student_section__section=exam.section).values_list("id", flat=True)
        invalid_students = [student_id for student_id in result.keys() if int(student_id) not in students]

        if invalid_students:
            raise serializers.ValidationError(
                f"الطلاب {invalid_students} لا ينتمون إلى الشعبة المحددة."
            )
        return data

    def create(self, validated_data):
        exam = validated_data.get("exam")
        result = validated_data.get("result")

        # إنشاء النتائج للطلاب
        results = []
        for student_id, score in result.items():
            student = Student.objects.get(id=student_id)
            student_result,_= StudentResult.objects.update_or_create(
                exam=exam, student=student
            )
            student_result.score=score
            student_result.save()
            results.append(student_result)

        return results
