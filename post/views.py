from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import Post
from .forms import ReviewForm


class AllPostView(ListView):
    model=Post
    template_name = 'home.html'

class PostCreateView(CreateView):
    model=Post
    template_name = 'new_post.html'
    fields=['author','title','text',]

class PostDetailView(DetailView):
    model=Post
    template_name = 'post_detail.html'

    from_class=ReviewForm
    success_url=reverse_lazy('home')


