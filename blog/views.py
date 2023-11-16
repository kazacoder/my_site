from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

home = '<br><a href="/">home</a>'
back = '<br><a href="..">back</a>'


def index(request):
    return HttpResponse('''
                        <h1>Главная страница</h1>
                        <a href="posts">Все посты</a>
                        ''')


def posts(request):
    return HttpResponse('Все посты блога' + back + home)


def posts_dynamic(request, post_name):
    return HttpResponse(f'Информация о посте <u><b>{post_name}</b></u>' + back + home)
