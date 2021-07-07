from rest_framework import serializers
from .models import Credito

class CreditosListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = [ 'id', 'nombre_empresa', 'monto']


class CreditoDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = '__all__'


class CreditoDecisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credito
        fields = ['aprobado', 'denegado']