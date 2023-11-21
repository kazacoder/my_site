from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'


def index(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


def posts(request):
    return HttpResponse('Все посты блога' + back + home)


def posts_dynamic(request, post_name):
    return HttpResponse(f'Информация о посте <u><b>{post_name}</b></u>' + back + home)


def posts_dynamic_by_number(request, post_number):
    return HttpResponse(f'Информация о посте под номером <u><b>{post_number}</b></u>' + back + home)