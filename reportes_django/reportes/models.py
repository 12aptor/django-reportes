from django.db import models
from datetime import datetime

# Create your models here.

class VentaModel(models.Model):
    id = models.AutoField(primary_key=True)
    ruc = models.CharField(max_length=11)
    razon_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=datetime.utcnow)

    def __str__(self) -> str:
        return self.razon_social

    class Meta:
        db_table = 'ventas'

  
class DetalleVentaModel(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    precio = models.FloatField()
    venta = models.ForeignKey(VentaModel, on_delete=models.CASCADE, related_name='detalleVenta')

    class Meta:
        db_table = 'detalles_venta'