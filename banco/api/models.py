from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    codigo = models.CharField(max_length=250)

    def json_object(self):
        return {
            "nome":self.nome,
            "endereco":self.endereco,
            "codigo":self.codigo
        }
    
    def __str_(self):
        return self.nome

class ClienteGerente(models.Model):
    codigo = models.CharField(max_length=250)
    codigoCliente = models.CharField(max_length=250)

    def json_object(self):
        return {
            "nome":self.codigo,
            "codigo":self.codigoCliente
        }
    
    def __str_(self):
        return self.codigo


class Ativo(models.Model):
    codigo = models.CharField(max_length=250,default="", editable=False)
    nome = models.CharField(max_length=250)
    modalidade = models.CharField(max_length=250)
    dataCriacao = models.CharField(max_length=250)
    clienteCriador=models.CharField(max_length=250)
    clienteCliente=models.CharField(max_length=250)

    def json_object(self):
        return {
            "codigo":self.codigo,
            "nome":self.nome,
            "modalidade":self.modalidade,
            "dataCriacao":self.dataCriacao,
            "codigoCriador":self.clienteCriador,
            "codigoCliente":self.clienteCliente
        }
    
    def __str_(self):
        return self.modalidade

class Transferencia(models.Model):
    ativo = models.CharField(max_length=250)
    codigoCliente = models.CharField(max_length=250)
    data = models.CharField(max_length=250)
    quantidade = models.FloatField()
    precoUnitario = models.FloatField()

    def json_object(self):
        return {
            "ativo":self.ativo,
            "codigoCliente":self.codigoCliente,
            "data":self.data,
            "quantidade":self.quantidade,
            "precoUnitario":self.precoUnitario,
        }

    def __str__(self):
        return "Transferencia de ativo {}".format(self.ativo)


class Retirada(models.Model):
    quantidade = models.FloatField()
    ativo = models.CharField(max_length=250)
    data = models.CharField(max_length=250)    
    precoUnitario = models.FloatField()

class Deposito(models.Model):
    quantidade = models.FloatField()
    ativo = models.CharField(max_length=250)
    data = models.CharField(max_length=250)    
    precoUnitario = models.FloatField()

class Saldo(models.Model):
    ativo = models.CharField(max_length=250)
    saldo = models.FloatField()

    def json_object(self):
        return {
            "ativo":self.ativo,
            "saldo":self.saldo,
        }

    def __str__(self):
        return "Transferencia de ativo {}".format(self.saldo)