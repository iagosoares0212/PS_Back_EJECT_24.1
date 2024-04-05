from django.shortcuts import render
from ..blog.models import Post
from django.http import HttpResponse

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-acessos')
    return render(request, 'index.html', {posts: posts})
    #return HttpResponse(posts[0].titulo+'\n'+posts[1].titulo+'\n'+posts[2].titulo)