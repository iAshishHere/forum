from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'forum_app/home.html')

