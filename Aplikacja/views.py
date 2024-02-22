from django.shortcuts import render


def post_list(request):
    posts = Post.objects.all()
    return "test 1234"

# Create your views here.
