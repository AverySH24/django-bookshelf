import json
from django.http import JsonResponse
from django.shortcuts import render
from  .models import Book, Genre
from django.views.decorators.csrf import csrf_exempt

def base(request):
    return render(request, 'book_app/base.html')

def list_genres(request):
    genres = Genre.objects.all()
    data = {"genres" : genres}
    return render(request, 'book_app/list_genres.html', data)

def list_books(request, genre_id):
    genre_books = Book.objects.all().filter(genre_id = genre_id)
    genre_name = Genre.objects.all().get(id = genre_id)
    data = {"books": genre_books, "genre": genre_name}
    return render(request, 'book_app/list_books.html', data)

def book_info(request, genre_id, book_id):
    book = Book.objects.all().get(id = book_id)
    data = {"book" : book,
    "genre_id": genre_id}
    return render(request, 'book_app/book_info.html', data)

@csrf_exempt
def add_book(request, genre_id):
    if request.method == "POST":
        body = json.loads(request.body)
        # MAKING BOOK OBJECT
        newBook = Book(title = body["title"], author = body["author"], description = body["description"], genre_id = genre_id)
        newBook.save()
        return JsonResponse({})
    # default get request
    return render(request, "book_app/add_book.html")

@csrf_exempt
def edit_book(request, genre_id, book_id):
    if request.method == "POST":
        body = json.loads(request.body)

        # get the book we want to change
        book = Book.objects.all().get(id = book_id)

        # Edit the information
        book.title = body['title']
        book.author = body['author']
        book.description = body['description']

        #save the information
        book.save()
        return JsonResponse({})
    # We need to pass this book because we want to populate the input values with its data
    data = {"book": Book.objects.all().get(id = book_id)}
    return render(request, "book_app/edit_book.html", data)