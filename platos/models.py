from django.db import models


# Create your models here.
class Platos(models.Model):
    nombre = models.CharField(max_length=40)
    precio = models.IntegerField(default=0)
    procedencia = models.CharField(max_length=40, default='Perú')

    def __str__(self):
        return "{}".format(self.nombre)
