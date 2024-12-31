from django.urls import path
from . import views

urlpatterns = [
    path('', views.prepare_attendance, name='start_attendance'),
    path('add_attendance/', views.add_attendance, name='add_attendance'),
    path('ajax/load-classes/', views.load_classes, name='load_classes'),
    path('ajax/load-sections/', views.load_sections, name='load_sections'),
    path('prepare_attendance/', views.prepare_attendance, name='prepare_attendance'),
    path('get_sections_by_class/', views.get_sections_by_class, name='get_sections_by_class'),
]


