# crudtp/urls.py
from django.urls import path
from .views import (
    AuthorListView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView,
    BlogPostListView, BlogPostCreateView, BlogPostUpdateView, BlogPostDeleteView
)

app_name = 'crudtp'

urlpatterns = [
    # URLs pour Author
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('author/create/', AuthorCreateView.as_view(), name='author_create'),
    path('author/update/<int:pk>/', AuthorUpdateView.as_view(), name='author_update'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='author_delete'),

    # URLs pour BlogPost
    path('blogposts/', BlogPostListView.as_view(), name='blogpost_list'),
    path('blogpost/create/', BlogPostCreateView.as_view(), name='blogpost_create'),
    path('blogpost/update/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost_update'),
    path('blogpost/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost_delete'),
]
