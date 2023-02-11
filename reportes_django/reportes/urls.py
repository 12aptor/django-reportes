from django.urls import path
from .views import ReporteVentasView, VentaPDFView

urlpatterns = [
    path('ventas', ReporteVentasView.as_view()),
    path('venta-pdf/<int:id>', VentaPDFView.as_view())
]