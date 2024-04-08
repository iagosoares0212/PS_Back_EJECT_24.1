from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Post


def blog(request: HttpRequest, num_posts: int = -1):
    # view do blog, recebe num_posts para efetuar o número de posts que serão exibidos (implementação do carregar mais)
    # o número default é -1 para conseguir com que, após clicar em carregar mais, o usuário continue ancorado na altura que estava antes
    # são exibidos apenas os posts públicos, em ordenados por número de acessos
    num_posts += 2
    posts = Post.objects.all().filter(public=True).order_by('-data_publicacao')
    return render(request, 'blog.html', {'posts': posts[:num_posts+1], 'num_posts': num_posts, 'search': ''})

def blog_search(request: HttpRequest, num_posts: int = -1):
    # view do blog com pesquisa, extrai os parametros da pesquisa através do GET e ordena os posts de acordo com a relevância
    num_posts += 2
    posts = Post.objects.all().filter(public=True)
    posts = order_search(posts, request.GET['q'])
    return render(request, 'blog.html', {'posts': posts[:num_posts+1], 'num_posts': num_posts, 'search': request.GET['q']})

def order_search(posts, search):
    # função que ordena os posts de acordo com a relevância da pesquisa
    search = search.strip().lower().split(' ')
    relevant_posts = []
    for post in posts:
        score = 0
        for word in search:
            # caso a palavra pesquisada esteja no título, valerá o dobro do que se estiver no subtítulo
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
    # view de um post individual, recebe o id do post e incrementa o número de acessos
    post = Post.objects.filter(public=True).get(id=id)
    post.acessos += 1
    post.save()
    return render(request, 'blogPostInd.html', {'post': post})