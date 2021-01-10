"""RESTful_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("",views.home,name="home"),
    path('all-cars/',views.all_cars,name="all_cars"),
    path("create-car/",views.post_car,name="post_car"),
    path('retrive-car/<str:car_name>/',views.get_car,name="get_car"),
    path('update-car/<str:car_name>/',views.put_car,name="update_car"),
    path('delete-car/<str:car_name>/',views.delete_car,name="delete_car"),
]
