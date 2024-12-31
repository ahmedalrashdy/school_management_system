from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import status
from school.models import Section
from students.serializers import StudentSerializer
from .models import StudentSection
class SectionStudentsView(APIView):
    def get(self, request, pk):
        try:
            section = Section.objects.filter(pk=pk).first()
            if not section:
                return Response(
                    {"error": "الشعبة غير موجودة."},
                    status=status.HTTP_404_NOT_FOUND
                )
            student_sections = StudentSection.objects.filter(section=section)
            students = [ss.student for ss in student_sections]  # استخراج قائمة الطلاب
            
            # تسلسل البيانات باستخدام StudentSerializer
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
