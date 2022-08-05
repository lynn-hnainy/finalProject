from pyexpat import model
from django.db import models
from books.models import Book
from members.models import Member
from datetime import timedelta
import datetime
# Create your models here.
class Borrowing(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.ForeignKey(Member,on_delete=models.CASCADE)
    borrow_date=models.DateField(default=datetime.datetime.now())
    return_date=models.DateField(blank=True, null=True)
    renew_borrowing=models.BooleanField(default=False)
    def clean(self):
        if not self.return_date:
            self.return_date = self.borrow_date + timedelta(days=10)


    def save(self, **kwargs):
        self.clean()
        return super().save(**kwargs)


    def __str__(self):
        return self.user.user.username+' '+self.book.book_title