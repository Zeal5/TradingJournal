from django.urls import path, include
from .views import UserRegistrationView,UserLoginView

urlpatterns = [
    path('',UserRegistrationView.as_view()),
    path('login/',UserLoginView.as_view()),
]