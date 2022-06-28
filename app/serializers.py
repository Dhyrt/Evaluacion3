from rest_framework import serializers
from app.models import *


class ProductoSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(required=True, min_length=5)
    codigo = serializers.IntegerField(required=True, min_value=100)
    precio = serializers.IntegerField(required=True, min_value=1000)

    
    class Meta:
        model = Producto
        fields = '__all__'