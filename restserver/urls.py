from django.urls import path, include
from . import views

urlpatterns = [
        path('login/', views.loginApp),
        path('signup/', views.signUp),
        path('getOffices/', views.getAllOffices),
        path('createOffice/', views.createOffice)
        ]
