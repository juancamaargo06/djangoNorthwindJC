# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InventarioRevendedor(models.Model):
    revendedor_email = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='revendedor_email', to_field='email')
    lote = models.ForeignKey('Lotes', models.DO_NOTHING)
    cantidad_disponible = models.IntegerField()
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_ingreso = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario_revendedor'


class Lotes(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad_piezas = models.IntegerField()
    precio_lote = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateTimeField(blank=True, null=True)
    revendedor_email = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='revendedor_email', to_field='email')
    descripcion = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lotes'


class PedidosRevendedor(models.Model):
    revendedor_email = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='revendedor_email', to_field='email')
    lote = models.ForeignKey(Lotes, models.DO_NOTHING)
    cantidad_solicitada = models.IntegerField()
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, blank=True, null=True)
    fecha_pedido = models.DateTimeField(blank=True, null=True)
    fecha_actualizacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pedidos_revendedor'


class Usuarios(models.Model):
    email = models.CharField(unique=True, max_length=255)
    password_hash = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'usuarios'


class VentasRevendedor(models.Model):
    revendedor_email = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='revendedor_email', to_field='email')
    lote = models.ForeignKey(Lotes, models.DO_NOTHING)
    cantidad_vendida = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    precio_total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_venta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ventas_revendedor'
