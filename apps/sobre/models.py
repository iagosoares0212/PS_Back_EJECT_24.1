from django.db import models

class Sobre(models.Model):
    nome = models.CharField(max_length=100)
    formacao = models.CharField(max_length=100)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='IMG')

    def __str__(self):
        return self.nome
    