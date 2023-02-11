from django.contrib import admin
from .models import VentaModel, DetalleVentaModel

# Register your models here.
class VentasAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'razon_social', 'direccion', 'created_at')

class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'descripcion', 'precio', 'venta')

admin.site.register(VentaModel, VentasAdmin)
admin.site.register(DetalleVentaModel, DetalleVentaAdmin)