from django.urls import path
from .views import SectionsWithExamsView, StudentResultCreateView

urlpatterns = [
    path('sections-with-exams/', SectionsWithExamsView.as_view(), name='sections-with-exams'),
    path('sections-with-exams/<int:pk>/', SectionsWithExamsView.as_view(), name='sections_with_exams'),
    path('create-student-results/', StudentResultCreateView.as_view(), name='create_student_results'),
]

