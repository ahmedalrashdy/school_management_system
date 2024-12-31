from django.urls import path
from .views import SectionStudentsView

urlpatterns = [
    path('section_students/<int:pk>/', SectionStudentsView.as_view(),name="section_students.index"),
]