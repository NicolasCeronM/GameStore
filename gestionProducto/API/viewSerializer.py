from .serializers import ProductoSerializer
from rest_framework import viewsets
from ..models import Producto

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer