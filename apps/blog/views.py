from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post

# Create your views here.
def blog(request: HttpRequest, num_posts: int = -1):
    num_posts += 2
    posts = Post.objects.all().filter(public=True)
    return render(request, 'blog.html', {'posts': posts[:num_posts+1], 'num_posts': num_posts, 'search': ''})

def blog_search(request: HttpRequest, num_posts: int = -1, search: str = ''):
    num_posts += 2
    posts = Post.objects.all().filter(public=True)
    posts = order_search(posts, request.GET['q'])
    return render(request, 'blog.html', {'posts': posts[:num_posts+1], 'num_posts': num_posts, 'search': request.GET['q']})

def order_search(posts, search):
    search = search.strip().lower().split(' ')
    relevant_posts = []
    for post in posts:
        score = 0
        for word in search:
            if word in post.titulo.lower():
                score += 2
            elif word in post.subtitulo.lower():
                score += 1
        if score > 0:
            relevant_posts.append((post, score))

    relevant_posts.sort(key=lambda x: x[1], reverse=True)
    for i in range(len(relevant_posts)):
        relevant_posts[i] = relevant_posts[i][0]
    return relevant_posts


def blog_post_individual(request: HttpRequest, id: int):

    post = Post.objects.filter(public=True).get(id=id)
    post.acessos += 1
    post.save()
    return render(request, 'blogPostInd.html', {'post': post})