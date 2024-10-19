from django.db import models

class Logs(models.Model):
    nombre = models.CharField(max_length=40)
    curso =  models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True) 
    
class Cronograma(models.Model): 
    estudiante = models.ForeignKey(Logs,on_delete=models.CASCADE,related_name='cronogramas') 
    fecha = models.DateField() 
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)