from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets

from .serializers import *
from .models import *


class AtivoViewSet(viewsets.ModelViewSet):
    queryset = Ativo.objects.all().order_by('nome')
    serializer_class = AtivoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer

class DepositoViewSet(viewsets.ModelViewSet):
    queryset = Deposito.objects.all().order_by('nome')
    serializer_class = DepositoSerializer

class RetiradaViewSet(viewsets.ModelViewSet):
    queryset = Retirada.objects.all().order_by('nome')
    serializer_class = RetiradaSerializer

class SaldoViewSet(viewsets.ModelViewSet):
    queryset = Saldo.objects.all().order_by('nome')
    serializer_class = SaldoSerializer

class TransferenciaViewSet(viewsets.ModelViewSet):
    queryset = Transferencia.objects.all().order_by('nome')
    serializer_class = TransferenciaSerializer