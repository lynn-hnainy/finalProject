from pyexpat import model
from django.db import models
from books.models import Book
from members.models import Member
from datetime import timedelta
import datetime
from django.contrib.auth.models import User
# Create your models here.
class Borrowing(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    borrow_date=models.DateField(default=datetime.datetime.now())
    return_date=models.DateField(blank=True, null=True)
    renew_borrowing=models.BooleanField(default=False)
    fines=models.IntegerField(default=0)
    def clean(self):
        if not self.return_date:
            self.return_date = self.borrow_date + timedelta(days=10)
        if not self.fines:
            self.fines = ((datetime.datetime.now().date()-self.return_date).days)*5


    def save(self, **kwargs):
        self.clean()
        return super().save(**kwargs)


    def __str__(self):
        return self.user.username+' '+self.book.book_title


class Reservation(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reservation_date= models.DateField(default=datetime.datetime.now())
    availability_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
