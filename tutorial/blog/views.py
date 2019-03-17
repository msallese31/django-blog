from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    # template_name required because we went against convention
    # convention would be: blog/post_list.html (or <app>/<model>_<viewtype>.html)
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # Order blogs newest to oldest
    ordering = ['-date_posted']
    paginate_by = 3


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_post.html'
    context_object_name = 'posts'
    # Order blogs newest to oldest
    paginate_by = 3

    def get_queryset(self):
        # get username from url query param
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Overridden
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Overridden
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})