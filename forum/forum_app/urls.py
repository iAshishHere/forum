from django.urls import path
from . import views
from .views import QuestionCreateView, QuestionDetailView

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/', QuestionDetailView.as_view(), name='detail'),
    path('create/', QuestionCreateView.as_view(), name='create'),
]