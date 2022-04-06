from django.urls import path
from .views import Home,signup,myBooks,addBook,update,delete

urlpatterns = [path('',Home.as_view(),name='home'),
               path('signup',signup,name='signup'),
               path('mybooks',myBooks,name='mybooks'),
               path('addbook',addBook,name='addbook'),
               path('update/<int:book_id>',update,name='update'),
               path('delete/<int:book_id>',delete,name='delete'),
               ]
