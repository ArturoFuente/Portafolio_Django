from django.db import models

# Create your models here.
from django.db import models

class PerfilProfesional(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    carrera = models.CharField(max_length=100)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
