from rest_framework import serializers
from .models import VentaModel, DetalleVentaModel

class DetallesVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleVentaModel
        exclude = ['venta']

class VentaSerializer(serializers.ModelSerializer):
    detalle = DetallesVentaSerializer(source='detalleVenta', many=True)
    class Meta:
        model = VentaModel
        fields = '__all__'