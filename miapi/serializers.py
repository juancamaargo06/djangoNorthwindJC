from rest_framework import serializers
from .models import InventarioRevendedor, Lotes, PedidosRevendedor, Usuarios, VentasRevendedor

class InventarioRevendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioRevendedor
        fields = '__all__'

class LotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lotes
        fields = '__all__'

class PedidosRevendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidosRevendedor
        fields = '__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'
class VentasRevendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = VentasRevendedor
        fields = '__all__'
