from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse

def index(request):
    return render(request, 'forum_app/home.html')


class PostDetailView(DetailView):
    model = Post
    #fields = ['questionTitle', 'questionContent']
    template_name = 'forum_app/post_detail.html'

class PostCreateView(CreateView):
    model = Post
    fields = ['questionTitle','questionContent']
    def get_success_url(self):
        return reverse('forum:detail',
                       args=[self.object.pk])
