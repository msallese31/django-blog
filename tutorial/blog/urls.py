from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    # TODO: Tie together content tabs.  Dynamically generate them from PostTypes
    path('tech/', PostListView.as_view(post_type_id=1), name="blog-tech"),
    path('digital-art/', PostListView.as_view(post_type_id=2), name="blog-art"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name="post-update"),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name="post-delete"),
    path('post/new/', PostCreateView.as_view(), name="post-create"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-posts"),
    path('about/', views.about, name="blog-about"),
]
