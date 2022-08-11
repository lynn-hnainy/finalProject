"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from members import views as member_views
from books import views as book_views
from booksTransaction import views as booksTrans_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', member_views.signin, name='login'),
    path('register/', member_views.register, name='register'),
    path('home/',book_views.home,name="home"),
    path('list_books/<cat_id>',book_views.list_books,name="list_books"),
    path('search/',book_views.search_books,name="search_books"),
    path('borrow/<book_id>/<user_id>',booksTrans_view.borrow_book,name="borrow_book"),
    path('borrowed_books/<user_id>',booksTrans_view.borrowed_books,name="borrowed_books"),
    path('renew_borrowing/<book_id>/<user_id>',booksTrans_view.renew_borrowing,name="renew_borrowing"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
