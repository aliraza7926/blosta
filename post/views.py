from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Post

class AllPostView(ListView):
    model=Post
    template_name = 'home.html'

class PostCreateView(CreateView):
    model=Post
    template_name = 'new_post.html'
    fields=['author','title','text',]
