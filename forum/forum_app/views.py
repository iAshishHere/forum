from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Question
from django.views.generic.edit import CreateView
from django.urls import reverse

def index(request):
    return render(request, 'forum_app/home.html')


class QuestionDetailView(DetailView):
    model = Question
    #fields = ['questionTitle', 'questionContent']
    template_name = 'forum_app/question_detail.html'

class QuestionCreateView(CreateView):
    model = Question
    fields = ['questionTitle','questionContent']
    def get_success_url(self):
        return reverse('forum:detail',
                       args=[self.object.pk])
