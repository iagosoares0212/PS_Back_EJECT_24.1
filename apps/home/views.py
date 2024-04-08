from django.shortcuts import render
from ..blog.models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')