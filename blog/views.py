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
    return render(request, 'blog/list_detail.html')


def posts_dynamic(request, post_name):
    return render(request, 'blog/detail_by_name.html', {'title': post_name})


def posts_dynamic_by_number(request, post_number):
    return render(request, 'blog/detail_by_number.html', {'number': post_number})