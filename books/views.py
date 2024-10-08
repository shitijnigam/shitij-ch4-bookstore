# from django.shortcuts import render
from typing import Any
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
)

# Create your views here.

from django.db.models.query import Q
from django.views.generic import ListView, DetailView

from .models import Book


class BookListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/book_list.html"
    # login_url = "account_login"


class BookDetailView(
    DetailView
):  # removed LoginRequiredMixin, PermissionRequiredMixin,
    model = Book
    context_object_name = "book"
    template_name = "books/book_detail.html"
    # login_url = "account_login"
    # permission_required = "books.special_status"
    queryset = Book.objects.all().prefetch_related(
        "reviews__author",
    )


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    # queryset = Book.objects.filter(title__icontains="beginners")

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(title__icontains=query)
        )
