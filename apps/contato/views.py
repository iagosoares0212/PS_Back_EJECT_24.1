from django.shortcuts import render
from .models import Contato

# Create your views here.
def contato(request):
    mensagemsalva = False
    if request.method == 'POST':
        contato = Contato(
            assunto=request.POST.get('assunto'),
            nome=request.POST.get('nome'),
            email=request.POST.get('email'),
            mensagem=request.POST.get('mensagem')
        )
        contato.save()
        mensagemsalva = True
    return render(request, 'contato.html', {'mensagemsalva': mensagemsalva})
    