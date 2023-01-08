from django.urls import path


from .views import ProductListCreateAPIView,ProductDetailAPIView

urlpatterns = [
    path('<slug>/',ProductDetailAPIView.as_view()),
    path('',ProductListCreateAPIView.as_view()),
]