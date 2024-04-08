from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    texto1 = models.TextField()
    texto2 = models.TextField()
    texto3 = models.TextField()
    foto_capa = models.ImageField(upload_to='IMG')
    foto_texto = models.ImageField(upload_to='IMG')
    acessos = models.IntegerField(default=0, editable=False)
    public = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo