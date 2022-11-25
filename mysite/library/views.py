from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Book, Author


def index(request):
    return HttpResponse("Hello, world. You're at the library index.")


class AuthorDetailView(DetailView):
    model = Author
    template_name = "library/author_detail.html"


class AuthorCreateView(CreateView):
    model = Author
    fields = ['name', 'birth_date']


class AuthorUpdateView(UpdateView):
    model = Author
    fields = ['name', 'birth_date']


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'library/author_confirm_delete.html'
    success_url = reverse_lazy('books:books_list')


class BookDetailView(DetailView):
    model = Book
    template_name = 'library/detail.html'


class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'pub_date']


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'author', 'pub_date']


class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('books:books_list')


def books_list(request):
    latest_books_list = Book.objects.order_by('-pub_date')
    context = {
        'latest_books_list': latest_books_list,
    }
    return render(request, 'library/index.html', context)
