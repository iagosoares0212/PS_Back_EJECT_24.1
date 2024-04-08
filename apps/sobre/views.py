from django.shortcuts import render
from .models import Sobre

def sobre(request):
    professores = Sobre.objects.all()
    return render(request, 'sobre.html', {'professores': professores})
