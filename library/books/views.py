from urllib import request
from django.shortcuts import render,redirect
from .models import Book, Category
from django.contrib import messages
# Create your views here.
cats=Category.objects.all()
def home(request):
    books=Book.objects.all()
    return render(request,'list_books.html',{'books':books,'cats':cats})

def list_books(request,cat_id):
    books=Book.objects.all().filter(cat_id=cat_id)
    if books:
        return render(request,'list_books.html',{'books':books,'cats':cats})
    else:
        messages.error(request, 'No books found!')
        return render(request,'list_books.html',{'cats':cats})

def search_books(request):
    if(request.method=="POST"):
        searched=request.POST['searched']
        books=Book.objects.filter(book_title__contains=searched)| Book.objects.filter(author_name__contains=searched)|Book.objects.filter(publication_year__contains=searched)
        if books:
            return render(request,'list_books.html',{'searched':searched,'books':books,'cats':cats})
        else:
            messages.error(request, 'No books found!')
            return render(request,'list_books.html',{'cats':cats})
    else:
        return render(request,'list_books.html',{'cats':cats})