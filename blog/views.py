from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Blog home</h1>")

posts = [
    {
        "author": "CoreyMs",
        "title": "Blog Post 1",
        "content": "first post content",
        "date_posted": "August 27, 2018",
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "second post content",
        "date_posted": "August 28, 2018",
    },
]


def home(request):
    context = {"posts": posts, }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {'title': 'About'})
