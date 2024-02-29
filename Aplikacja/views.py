from django.http import HttpResponse
from django.shortcuts import render

from Aplikacja.models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request,'blog/post/list.html')


# Create your views here.
