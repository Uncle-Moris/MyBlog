from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post


def posts_list(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request,'posts/list.html', context)


def posts_details(request):
    post_details = Post.objects.first()
    context = {'details': post_details}
    return render(request, 'posts/details.html', context)

