from urllib import request
from django.shortcuts import render,redirect
from .models import Book, Category
# Create your views here.
cats=Category.objects.all()
def home(request):
    books=Book.objects.all()
    return render(request,'home.html',{'books':books,'cats':cats})

def list_books(request,cat_id):
    books=Book.objects.all().filter(cat_id=cat_id)
    return render(request,'list_books.html',{'books':books,'cats':cats})

def search_books(request):
    if(request.method=="POST"):
        searched=request.POST['searched']
        books=Book.objects.filter(book_title__contains=searched)| Book.objects.filter(author_name__contains=searched)|Book.objects.filter(publication_year__contains=searched)
        return render(request,'search_books.html',{'searched':searched,'books':books,'cats':cats})
    else:
         return render(request,'search_books.html',{'cats':cats})