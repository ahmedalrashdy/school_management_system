from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from school.models import AcademicYear, ClassLevel
from school.serializers import ClassLevelSerializer

class ClassLevelListView(APIView):
    def get(self, request):
        try:
            current_year = AcademicYear.get_current_year()
            if not current_year:
                return Response(
                    {"error": "لا يمكن العثور على السنة الحالية."}, 
                    status=status.HTTP_400_BAD_REQUEST
                )

            # جلب جميع المستويات الدراسية
            class_levels = ClassLevel.objects.all()

            # تمرير البيانات إلى Serializer مع السياق
            serializer = ClassLevelSerializer(class_levels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
