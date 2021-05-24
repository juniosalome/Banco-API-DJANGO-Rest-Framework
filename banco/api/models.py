from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)
    codigo = models.CharField(max_length=250,default="", editable=False)

    def json_object(self):
        return {
            "nome":self.nome,
            "endereco":self.endereco,
            "codigo":self.codigo
        }
    
    def __str_(self):
        return self.nome

class ClienteGerente(models.Model):
    codigo = models.CharField(max_length=250,default="", editable=False)
    codigoCliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)

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
    clienteCriador=models.ForeignKey('ClienteGerente',on_delete=models.CASCADE)
    clienteCliente=models.ForeignKey('Cliente',on_delete=models.CASCADE)

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
    ativo = models.ForeignKey('Ativo',on_delete=models.CASCADE)
    codigoCliente = models.ForeignKey('Cliente',on_delete=models.CASCADE)
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
        return "Transferencia de ativo {}".format(self.ativo.nome)


class Retirada(models.Model):
    quantidade = models.FloatField()
    ativo = models.ForeignKey('Ativo',on_delete=models.CASCADE)
    data = models.CharField(max_length=250)    
    precoUnitario = models.FloatField()

class Deposito(models.Model):
    quantidade = models.FloatField()
    ativo = models.ForeignKey('Ativo',on_delete=models.CASCADE)
    data = models.CharField(max_length=250)    
    precoUnitario = models.FloatField()

class Saldo(models.Model):
    ativo = models.ForeignKey('Ativo',on_delete=models.CASCADE)