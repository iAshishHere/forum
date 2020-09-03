from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
from .models import Question, QuestionComment, Answer
from django.views.generic.edit import CreateView
from django.urls import reverse
from django.views.generic import ListView

def index(request):
    return render(request, 'forum_app/home.html')


# class QuestionDetailView(DetailView):
#     model = Question
#     queryset = Question.objects.all()
#
#     #model = QuestionComment
#     #fields = ['questionTitle', 'questionContent']
#     template_name = 'forum_app/question_detail.html'


class QuestionDetailView(DetailView):
    #context_object_name = 'detail'
    model = Question

  #  fields = ['questionTitle', 'questionContent']
    template_name = 'forum_app/question_detail.html'
    #queryset = Question.objects.filter(id=3)

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        q = Question.objects.get(pk=self.object.pk)
        context['answer'] = q.answer_set.all()
        return context

class QuestionCreateView(CreateView):
    model = Question
    fields = ['questionTitle','questionContent']
    def get_success_url(self):
        return reverse('forum:detail',
                       args=[self.object.pk])

