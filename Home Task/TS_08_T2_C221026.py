from django.shortcuts import render

# Create your views here.

from django.views import View
from django.http import HttpResponse
from django.views.generic import ListView
from books.models import Book

class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django from class")
    
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    