from django.urls import path
from . import views
from .views import PostCreateView, PostDetailView

app_name = 'forum'
urlpatterns = [
    path('', views.index, name='home'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('create/', PostCreateView.as_view(), name='create'),
]