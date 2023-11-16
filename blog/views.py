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
