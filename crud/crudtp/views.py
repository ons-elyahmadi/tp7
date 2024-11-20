# crudtp/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Author, BlogPost

# Vues pour Author
class AuthorListView(ListView):
    model = Author
    context_object_name = 'authors'
    template_name = 'crudtp/author_list.html'

class AuthorCreateView(CreateView):
    model = Author
    fields = ['user', 'bio', 'profile_picture']
    template_name = 'crudtp/author_create.html'
    success_url = reverse_lazy('crudtp:author_list')

class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['user', 'bio', 'profile_picture']
    template_name = 'crudtp/author_update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('crudtp:author_list')

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'crudtp/author_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('crudtp:author_list')

# Vues pour BlogPost
class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'posts'
    template_name = 'crudtp/blogpost_list.html'

class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ['title', 'content', 'author', 'created_on']
    template_name = 'crudtp/blogpost_create.html'
    success_url = reverse_lazy('crudtp:blogpost_list')

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    fields = ['title', 'content', 'author']
    template_name = 'crudtp/blogpost_update.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('crudtp:blogpost_list')

class BlogPostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'crudtp/blogpost_delete.html'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('crudtp:blogpost_list')
