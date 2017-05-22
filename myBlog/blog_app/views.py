from django.shortcuts import render
from .models import Post
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from django.http import HttpResponse


def index(request):
    all_posts = Post.objects.all()
    print(all_posts)
    return render(request, 'index.html', {'all_posts': all_posts})


def single_post(request, pk):
    post_detail = Post.objects.get(id=pk)
    print('single_post', post_detail)
    return render(request, 'post_detail.html', {'post_detail': post_detail})


class PostUpdate(UpdateView):
    model = Post
    template_name = 'post_update.html'
    fields = '__all__'
    success_url = reverse_lazy('index')
