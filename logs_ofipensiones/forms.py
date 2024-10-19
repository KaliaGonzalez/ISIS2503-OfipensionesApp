from django import forms
from .models import Logs

class LogsForm(forms.ModelForm):
    class Meta:
        model = Logs
        fields = [
            'nombre',
            'curso',
            'identificacion', 
            #'dateTime',
        ]

        labels = {
            'nombre' : 'Nombre',
            'curso' : 'Curso',
            'identificacion' : 'Identificacion',
            #'dateTime' : 'Date Time',
        }
