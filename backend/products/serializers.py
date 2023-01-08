from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        lookup_field = 'slug'
        fields = [
            'pk',
            'title',
            'price',
            'sale_price',
            "content",
            "slug",
            'my_discount']


    def get_my_discount(self,obj):
        if not hasattr(obj,'id'):
            return None
        return obj.get_discount()
        