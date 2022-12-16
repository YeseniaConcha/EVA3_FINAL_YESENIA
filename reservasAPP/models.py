from django.db import models

# Create your models here.
# modelo para reservas 

class Reservas(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)
    hora = models.TimeField(auto_now_add=True)
    cantidad = models.IntegerField()
    estado = models.CharField(max_length=50)
    observacion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "reserva"
        verbose_name_plural = "reservas"

    def __str__(self):
        return self.nombre











