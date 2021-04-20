from django.urls import path, include
from .views import userRegister

urlpatterns = [
    path('register/', userRegister.as_view(), name='register'),
    
]