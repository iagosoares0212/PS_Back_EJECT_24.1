from django.db import models

class Curso(models.Model):
    TIPO_CURSO_CHOICES = [
        ('CH', 'Ciências Humanas'),
        ('CE', 'Ciências Exatas'),
        ('BIO', 'Biociências'),
    ]
    
    tipo_curso = models.CharField(max_length=3, choices=TIPO_CURSO_CHOICES)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    numero_parcelas = models.IntegerField()
    preco_parcela = models.DecimalField(max_digits=10, decimal_places=2)
    preco_vista = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='IMG')
    avaliacoes = models.DecimalField(max_digits=2, decimal_places=1)

    def __str__(self):
        return self.titulo
    
class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='IMG')
    texto1 = models.CharField(max_length=100)
    texto2 = models.CharField(max_length=100)

    def __str__(self):
        return self.nome