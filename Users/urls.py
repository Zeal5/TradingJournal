from django.urls import path, re_path
from .views import first

urlpatterns =[
    path("",first,name="index"),
]