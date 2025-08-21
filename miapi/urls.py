from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomersViewSet, ProductsViewSet, OrdersViewSet, OrderdetailsViewSet

router = DefaultRouter()
router.register(r'customers', CustomersViewSet)
router.register(r'products', ProductsViewSet)
router.register(r'orders', OrdersViewSet)
router.register(r'orderdetails', OrderdetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
