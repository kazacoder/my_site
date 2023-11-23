from random import choices
from django.shortcuts import render
from .posts import posts as posts_list

# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'


def index(request):
    context = {'posts': choices(posts_list, k=3)}
    return render(request, 'blog/index.html', context)


def posts(request):
    return render(request, 'blog/list_detail.html')


def posts_dynamic(request, post_name):
    return render(request, 'blog/detail_by_name.html', {'title': post_name})


def posts_dynamic_by_number(request, post_number):
    return render(request, 'blog/detail_by_number.html', {'number': post_number})

