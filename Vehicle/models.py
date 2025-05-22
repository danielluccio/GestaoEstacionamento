
# Create your models here.
from django.db import models
from Customers.models import Customer

# Classe de Tipo do Veiculo !

class VehicleType(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome")
    description = models.TextField(default="Veiculo sem Descrição", verbose_name="Descrição")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Tipo de Veiculo"
        verbose_name_plural = "Tipos de Veiculos"
        db_table = "Tipo de Veiculo"

    def __str__(self):
        return self.name
    

# Classe para Veiculos

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.PROTECT, blank=True, null=True, related_name="vehicles", verbose_name="Tipo do Veiculo")
    license_plate = models.CharField(max_length=20, unique=True, verbose_name="Placa do Veículo")
    brand = models.CharField(max_length=50, verbose_name="Marca", blank=True, null=True)
    model = models.CharField(max_length=100, verbose_name="Modelo", blank=True, null=True)
    color = models.CharField(max_length=30, verbose_name="Cor", blank=True, null=True)
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT, blank=True, null=True, related_name="vehicles", verbose_name="Propietário")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Criado em")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Atualizado em")

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        db_table = "Veículos"

    def __str__(self):
        return self.license_plate
