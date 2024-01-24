from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=35)
    credito=models.PositiveIntegerField()
    
    def __str__(self) -> str:
        texto = '{0} ({1})'
        return texto.format(self.nombre, self.credito)