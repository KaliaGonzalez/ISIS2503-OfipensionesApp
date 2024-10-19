from django.db import models

class Logs(models.Model):
    nombre = models.CharField(max_length=40)
    curso =  models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    dateTime = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return '%s %s' % (self.value, self.unit)