from re import template
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Books

# Create your views here.

class BookListView(ListView):
    model = Books
    template_name = 'bookss/book_list.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Books
    template_name = 'bookss/book_detail.html'
    context_object_name = 'book'

