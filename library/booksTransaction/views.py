from urllib import request
from django.shortcuts import render,redirect
from books.models import Book
from members.models import Member
from .models import Borrowing
from django.contrib.auth.models import User
# Create your views here.
def borrow_book(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    borrow=Borrowing.objects.create(book=book,user=member)
    return render(request,"borrowed.html")