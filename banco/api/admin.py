from django.contrib import admin


# Register your models here.
from .models import *
admin.site.register(Ativo)
admin.site.register(Cliente)
admin.site.register(Deposito)
admin.site.register(Retirada)
admin.site.register(Saldo)
admin.site.register(Transferencia)