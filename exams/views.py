from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Section
from .serializers import SectionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import StudentResultInputSerializer


class StudentResultCreateView(APIView):
    def post(self, request):
        serializer = StudentResultInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "تم حفظ النتائج بنجاح."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SectionsWithExamsView(APIView):
    def get(self, request,pk=None):
        try:
            if pk is not None:
                section = Section.objects.filter(pk=pk).first()
                if not section:
                    return Response(
                        {"error": "الشعبة غير موجودة."},
                        status=status.HTTP_404_NOT_FOUND
                    )
                serializer = SectionSerializer(section)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            sections = Section.objects.all()
            serializer = SectionSerializer(sections, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        


class StudentResultCreateView(APIView):
    def post(self, request):
        print("*"*100)
        print(request.data)
        print("*"*100)
        serializer = StudentResultInputSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "تم حفظ النتائج بنجاح."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

