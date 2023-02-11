from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import VentaModel
from .serializers import VentaSerializer
from datetime import datetime
from django.http import HttpResponse
import mimetypes
import os
import fitz

# Create your views here.

class ReporteVentasView(generics.GenericAPIView):
    queryset = VentaModel.objects.all()
    serializer_class = VentaSerializer

    def get(self, request):
        desde = "2023-02-11"
        hasta = "2023-02-12"
        desde_splited = desde.split("-")
        hasta_splited = hasta.split("-")
        record = self.serializer_class(
            self.get_queryset().filter(
              created_at__gt=datetime(
                int(desde_splited[0]),
                int(desde_splited[1]),
                int(desde_splited[2])
              ),
              created_at__lt=datetime(
                int(hasta_splited[0]),
                int(hasta_splited[1]),
                int(hasta_splited[2]) + 1
              )
            ),
            many=True
        )
        response = []
        last_date = ""
        ventas_by_date = []
        for venta in record.data:
            created_at_date = venta['created_at'][:10]
            if created_at_date == last_date:
                last_date = created_at_date
                ventas_by_date.append(venta)
            else:
                ventas_by_date = []
                ventas_by_date.append(venta)
                last_date = created_at_date
                if len(response) == 0 and len(ventas_by_date) == 0:
                    continue
                response.append({
                    'created_at': last_date,
                    'ventas': ventas_by_date
                })
        return Response(data=response, status=status.HTTP_200_OK)
    
class VentaPDFView(generics.GenericAPIView):
    queryset = VentaModel.objects.all()
    serializer_class = VentaSerializer

    def get(self, request, id):
        try:
          record = self.serializer_class(self.get_queryset().get(id=id))
          pdf = fitz.open()
          page = pdf.new_page(pno=-1, width=595, height=842)
          page.draw_rect(rect=(10, 10, 585, 300), color=(0,0,0), fill=(1,1,1), overlay=True)
          y_inicial = 50
          for articulo in record.data['detalle']:
              page.insert_text(fitz.Point(20, y_inicial), articulo['descripcion'], fontsize=16)
              y_inicial += 20
          pdf.write()
          pdf.save("pdf-prueba.pdf", pretty=True)

          BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
          filename = 'pdf-prueba.pdf'
          filepath = BASE_DIR + '/' + filename
          path = open(filepath, 'r')
          mime_type, _ = mimetypes.guess_type(filepath)
          response = HttpResponse(path, content_type=mime_type)
          response['Content-Disposition'] = "attachment; filename=%s" % filename
          return response
        
        except Exception as e:
            return Response(data={
                'message': 'Internal server error',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)       