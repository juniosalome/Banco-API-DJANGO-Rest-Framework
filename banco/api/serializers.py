from rest_framework import serializers 

from .models import * 

class AtivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ativo
        fields = ('__all__')

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('__all__')

class DepositoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposito
        fields = ('__all__')

class RetiradaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retirada
        fields = ('__all__')

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = ('__all__')

class TransferenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transferencia
        fields = ('__all__')
