from django.db import models

# Classe de Tipo do Veiculo !

class VehicleType(models.Model):
    name = models.CharField(max_length=100, )
