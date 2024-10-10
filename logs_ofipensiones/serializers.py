from rest_framework import serializers
from . import models


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('nombre', 'descripcion', 'accion',)
        model = models.Logs