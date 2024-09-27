from django.contrib import admin
from django.urls import path,include
from app1.views import EmployeeView

urlpatterns = [
    path("",EmployeeView.as_view()),

]