from django import forms
from .models import Logs

class LogsForm(forms.ModelForm):
    class Meta:
        model = Logs
        fields = [
            'nombre',
            'descripcion',
            'accion',
            #'dateTime',
        ]

        labels = {
            'nombre' : 'Nombre',
            'descripcion' : 'Descripcion',
            'accion' : 'Accion',
            #'dateTime' : 'Date Time',
        }
