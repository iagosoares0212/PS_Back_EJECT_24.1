from django.db import models

# Create your models here.
class Contato (models.Model):
    ASSUNTO_CHOICES = [
        ('a', 'Ajuda'),
        ('e', 'Elogio'),
        ('s', 'Sugestão')
    ]
    
    assunto = models.CharField(max_length=1, choices=ASSUNTO_CHOICES)
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.assunto
