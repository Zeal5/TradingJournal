from django.urls import path
from .views import first

urlpatterns =[
    path("<int:id>",first,name="index"),
    path("<int:id>/<int:args>/",first,name="index")
]