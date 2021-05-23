from django.shortcuts import render

# Create your views here.


from rest_framework import viewsets

from .serializers import ClienteSerializer
from .models import Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all().order_by('nome')
    serializer_class = ClienteSerializer