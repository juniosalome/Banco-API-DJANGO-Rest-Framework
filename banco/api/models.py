from django.db import models

# Create your models here.


class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    endereco = models.CharField(max_length=250)

    def json_object(self):
        return {
            "nome":self.nome,
            "endereco":self.endereco
        }

    def __str_(self):
        return self.nome