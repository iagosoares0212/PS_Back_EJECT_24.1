from django.shortcuts import render
from .models import Curso,Aluno

def curso(request):
    cursos = Curso.objects.all()
    cursos_ciencias_humanas = Curso.objects.filter(tipo_curso='CH')
    cursos_ciencias_exatas = Curso.objects.filter(tipo_curso='CE')
    cursos_biociencias = Curso.objects.filter(tipo_curso='BIO')
    return render(request, 'cursos.html', {'cursos': cursos,'cursos_ciencias_humanas': cursos_ciencias_humanas,'cursos_ciencias_exatas': cursos_ciencias_exatas,'cursos_biociencias': cursos_biociencias})

def todos_cursos_ciencias_humanas(request):
    cursos_ciencias_humanas = Curso.objects.filter(tipo_curso='CH')
    return render(request,'cursos.html' , {'cursos_ciencias_humanas': cursos_ciencias_humanas})

def todos_cursos_ciencias_exatas(request):
    cursos_ciencias_exatas = Curso.objects.filter(tipo_curso='CE')
    return render(request, 'cursos.html', {'cursos_ciencias_exatas': cursos_ciencias_exatas})

def todos_cursos_biociencias(request):
    cursos_biociencias = Curso.objects.filter(tipo_curso='BIO')
    return render(request, 'cursos.html', {'cursos_biociencias': cursos_biociencias})


def cursos_populares(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos.html', {'cursos': cursos})

def lista_alunos(request):
    alunos = Aluno.objects.all()  
    return render(request, 'cursos.html', {'alunos': alunos})
