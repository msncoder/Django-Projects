from django.urls import path
from . import views

urlpatterns = [
    path('skills/', views.Skills, name="skills page")
]
