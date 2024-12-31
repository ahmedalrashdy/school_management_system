from django.urls import path
from .views import ClassLevelListView

urlpatterns = [
    path('class_levels/', ClassLevelListView.as_view(),name="class_levels.index"),
]