from django.urls import path
from .views import first

urlpatterns =[
    path("<int:id>",first)
]