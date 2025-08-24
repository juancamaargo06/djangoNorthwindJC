from rest_framework import routers
from django.urls import path, include
from .views import InventarioRevendedorViewSet, LotesViewSet, PedidosRevendedorViewSet, UsuariosViewSet, VentasRevendedorViewSet

router = routers.DefaultRouter()
router.register(r'inventariorevendedor', InventarioRevendedorViewSet)
router.register(r'lotes', LotesViewSet)
router.register(r'pedidosrevendedor', PedidosRevendedorViewSet)
router.register(r'usuarios', UsuariosViewSet)
router.register(r'ventasrevendedor', VentasRevendedorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
