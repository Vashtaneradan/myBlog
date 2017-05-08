from django.shortcuts import render
from .models import Post

from django.http import HttpResponse


def index(request):
    all_posts = Post.objects.all()
    return render(request, 'index.html', {'all_posts': all_posts})


