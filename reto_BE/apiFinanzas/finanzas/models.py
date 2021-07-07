from django.db import models
from django.contrib.auth.models import User
from .utils import IntegerRangeField
# Create your models here.



class Trabajador(models.Model):
    user     = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nombre   = models.CharField(max_length=255, blank=True, null=True)
    apellido = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Credito(models.Model):
    PUNTUACIONES        = [('mala', 'mala'), ('regular', 'regular'), ('buena', 'buena')]
    nombre_empresa      = models.CharField(max_length=255, blank=True, null=True)
    monto               = IntegerRangeField(min_value=0, max_value=50000)
    deudaSBS            = models.IntegerField(blank=True, null=True)
    puntuacionSentinel  = models.CharField(max_length=7, choices=PUNTUACIONES, default='regular')
    puntuacionIA        = IntegerRangeField(min_value=1, max_value=10)
    aprobado            = models.BooleanField(default=False)
    denegado            = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.nombre_empresa} - {self.monto}$'

