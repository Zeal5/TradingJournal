from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer



#create using post and get data for all the items in db using get method
class ProductListCreateAPIView(generics.ListCreateAPIView):
    query_pk_and_slug = True
    queryset = Product.objects.all()
    serializer_class = ProductSerializer 

#get data for specific product using prodocuts/<int>/ endpoint
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

