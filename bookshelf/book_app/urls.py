from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Display for default runserver
    path("", views.base, name = "base"), 
    # Shows list of genres
    path("genres/", views.list_genres, name = "list_genres"),
    # List books
    path('genres/<int:genre_id>/', views.list_books, name = "list_books"),
    # Shows specific book info
    path('genres/<int:genre_id>/books/<int:book_id>/', views.book_info, name = "book_info"),
    # GET: Shows form for input, POST: creates new Book object and saves data to database
    path('genres/<int:genre_id>/books/new/', views.add_book, name = "add_book"),
    # GET: Shows form for input with populated fields, POST: gets existing book object and saves data to database
    path('genres/<int:genre_id>/books/<int:book_id>/edit/', views.edit_book, name = "edit_book")
]