from rest_framework import serializers
from reservasAPP.models import *

class reservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservas
        fields = '__all__'