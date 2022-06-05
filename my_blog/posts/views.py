from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post


def posts_list(request):
    posts_list = Post.objects.all()
    context = {'posts_list': posts_list}
    return render(request,'posts/posts_list.html', context=context)

