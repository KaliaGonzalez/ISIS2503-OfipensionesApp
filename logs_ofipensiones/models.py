from django.db import models

class Logs(models.Model):
    nombre = models.CharField(max_length=40)
    descripcion =  models.CharField(max_length=50)
    accion = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.value, self.unit)