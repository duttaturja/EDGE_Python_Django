from django.urls import path
from books.views import (
    MyView, BookListView, ContactFormView, BookCreateView,
    APIBook ,APIAuthor, APIPublisher,
      BookGetUpdateDelete)                     
from django.shortcuts import render
from user import views as user_views


urlpatterns = [
    path('initial_class/', MyView.as_view()),
    path('list/', BookListView.as_view()),
    path('contact/add', ContactFormView.as_view()),
    path('contact_success/', lambda request: render(request, 'success/contact_success.html'), name='contact_success'),
    path('add/', BookCreateView.as_view(), name = 'book_add'),
    path('user/profile/', user_views.profile_view, name='profile'),
    path('books_rest/', APIBook.as_view(), name='book_list_create'),
    path('rest/book/<int:pk>', BookGetUpdateDelete.as_view(), name='rest_book'),
    path('authors_rest/', APIAuthor.as_view(), name='author_list_create'),
]