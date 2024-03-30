from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=500)
    autor = models.CharField(max_length=50)
    data_publicação = models.DateTimeField(auto_now_add=True)
    texto = models.TextField()
    foto_capa = models.ImageField(upload_to='media')
    foto_texto = models.ImageField(upload_to='media')

    def __str__(self):
        return self.titulo