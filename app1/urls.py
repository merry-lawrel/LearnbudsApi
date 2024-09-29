from django.contrib import admin
from django.urls import path,include
from app1.views import EmployeeView, RegisterAPI, LoginAPI, Employee

urlpatterns = [
    path("",EmployeeView.as_view()),
    path("register/",RegisterAPI.as_view()),
    path("login/",LoginAPI.as_view()),
    path("employee/",Employee.as_view())

]