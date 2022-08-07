from urllib import request
from django.shortcuts import render,redirect
from books.models import Book
from django.contrib import messages
from .models import Borrowing
from django.contrib.auth.models import User
# Create your views here.
def borrow_book(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    if Borrowing.objects.filter(book=book) and Borrowing.objects.filter(user=member).exists():
        messages.error(request, 'Book already borrowed')
        return redirect('home')
    else:
        book.number_of_copies-=1
        book.save()
        borrow=Borrowing.objects.create(book=book,user=member)
        return render(request,"borrowed_successfully.html")

def borrowed_books(request,user_id):
    member=User.objects.get(id=user_id)
    borrowed_books=Borrowing.objects.filter(user=member)
    return render(request,"borrowed.html",{'books':borrowed_books})