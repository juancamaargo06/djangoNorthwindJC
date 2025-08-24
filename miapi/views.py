from rest_framework import viewsets
from .models import InventarioRevendedor, Lotes, PedidosRevendedor, Usuarios, VentasRevendedor
from .serializers import InventarioRevendedorSerializer, LotesSerializer, PedidosRevendedorSerializer, UsuariosSerializer, VentasRevendedorSerializer

class InventarioRevendedorViewSet(viewsets.ModelViewSet):
    queryset = InventarioRevendedor.objects.all()
    serializer_class = InventarioRevendedorSerializer

class LotesViewSet(viewsets.ModelViewSet):
    queryset = Lotes.objects.all()
    serializer_class = LotesSerializer

class PedidosRevendedorViewSet(viewsets.ModelViewSet):
    queryset = PedidosRevendedor.objects.all()
    serializer_class = PedidosRevendedorSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset = Usuarios.objects.all()
    serializer_class = UsuariosSerializer

class VentasRevendedorViewSet(viewsets.ModelViewSet):
    queryset = VentasRevendedor.objects.all()
    serializer_class = VentasRevendedorSerializer
