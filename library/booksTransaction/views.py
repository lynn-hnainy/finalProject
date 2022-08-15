from urllib import request
from django.shortcuts import render,redirect
from books.models import Book,Category
from django.contrib import messages
from .models import Borrowing, Reservation
from django.contrib.auth.models import User
from datetime import timedelta
import datetime
cats=Category.objects.all()
# Create your views here.
def borrow_book(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    borrow=Borrowing.objects.filter(book=book).filter(user=member)
    if borrow:
        messages.error(request, 'Book already borrowed')
        return redirect('home')
    else:
        book.number_of_copies-=1
        book.save()
        borrow=Borrowing.objects.create(book=book,user=member)
        return render(request,"borrowed_successfully.html",{'cats':cats})

def borrowed_books(request,user_id):
    member=User.objects.get(pk=user_id)
    borrowed_books=Borrowing.objects.filter(user=member)
    return render(request,"borrowed.html",{'books':borrowed_books,'cats':cats})


def reserved_books(request,user_id):
    member=User.objects.get(pk=user_id)
    reserved_books=Reservation.objects.filter(user=member)
    return render(request,"reserved.html",{'books':reserved_books,'cats':cats})

def renew_borrowing(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    borrowed_books=Borrowing.objects.filter(user=member)
    borrowed_book=Borrowing.objects.get(user=member,book=book)
    borrowed_book.renew_borrowing=True
    borrowed_book.return_date+=timedelta(days=10)
    borrowed_book.save()
    return render(request,"borrowed.html",{'books':borrowed_books,'cats':cats})

def reserve_book(request,book_id,user_id):
    book=Book.objects.get(pk=book_id)
    member=User.objects.get(id=user_id)
    reserve=Reservation.objects.filter(book=book).filter(user=member)
    if reserve:
        messages.error(request, 'Book already reserved')
        return redirect('home')
    else:
        reserve=Reservation.objects.create(book=book,user=member)
        return render(request,"reserved_successfully.html",{'cats':cats})
