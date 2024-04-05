from django.urls import path, URLPattern
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:num_posts>', views.blog, name='blogcarregarmais'),
    path('search', views.blog_search, name='blogsearch'),
    path('<int:num_posts>/search', views.blog_search, name='blogsearchmais'),
    path('post/<int:id>', views.blog_post_individual, name='post')
]