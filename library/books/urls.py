from django import views
from django.urls import path, re_path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('list_books/<cat_id>',views.list_books,name="list_books"),
    path('search',views.search_books,name="search_books"),
]