from django.urls import path
from .views import first

urlpatterns =[
    path("<int:id>/<str:name>",first)
]