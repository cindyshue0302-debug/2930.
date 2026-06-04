"""
URL configuration for backend project.
"""
from django.contrib import admin
from django.urls import path
from api import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
   
    path('api/quiz/submit/', views.save_quiz_score), 
]