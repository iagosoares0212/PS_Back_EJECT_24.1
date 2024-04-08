# Crie um arquivo urls.py dentro do diretório 'apps/cursos' se ainda não existir

from django.urls import path
from . import views
app_name="sobre"
urlpatterns = [
    path('', views.sobre, name='sobre')
]

