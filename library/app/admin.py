from django.contrib import admin
from .models import BookType,Book

# Register your models here.

class BookT(admin.ModelAdmin):
    list_display=('id','book_type')

class Books(admin.ModelAdmin):
    list_display=('user','bookName','author','bookType')


admin.site.register(BookType,BookT)
admin.site.register(Book,Books)
