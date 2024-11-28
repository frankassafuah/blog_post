from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

# FUNCTION BASED VIEWS
# def home(request):
#     return HttpResponse("<h1>Blog home</h1>")


def home(request):
    context = {
        "posts": Post.objects.all(),
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})


# CLASS BASED VIEWS
# listView, DetailView, UpdateView, DeleteView


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"  # by default django view look for <app>/<model>_<viewtype>.html
    context_object_name = "posts"  # by default the PostListView will call our context 'object' instead of 'posts'
    ordering = [
        "-date_posted"
    ]  # orders our post from newes to oldest ( remove - sign if you want to order from oldest to newest)


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # UserPassesTestMixin will run this test_func method
    def test_func(self):
        post = self.get_object()  # this gets the post we are currently trying to update

        # check if the user trying to update this post is the creator of this post
        if self.request.user == post.author:
            return True

        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # UserPassesTestMixin will run this test_func method
    def test_func(self):
        post = self.get_object()  # this gets the post we are currently trying to delete

        # check if the user trying to delete this post is the creator of this post
        if self.request.user == post.author:
            return True

        return False
