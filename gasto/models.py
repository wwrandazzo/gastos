from django.db import models

# Create your models here.
class Gasto (models.Model):
    categoria = models.CharField(max_length=50)
    importe = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateField()
    descripcion = models.TextField()

    def __str__(self):
        return self.descripcion
    
    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'
        ordering = ['-fecha']