from re import template
from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.mixins import (LoginRequiredMixin, PermissionRequiredMixin)
from django.views.generic import ListView, DetailView
from .models import Books

# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'bookss/book_list.html'
    context_object_name = 'books'
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Books
    template_name = 'bookss/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'bookss.special_status'

class SearchResultsView(ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'bookss/search_results.html'
    # queryset = Books.objects.filter(title__icontains='beginners')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Books.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
