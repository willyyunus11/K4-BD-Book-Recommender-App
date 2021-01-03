from django.contrib import admin
from django.utils.html import format_html

# Register your models here.

from .models import Book

admin.AdminSite.site_header = "Book Recommendation System Administrator"
admin.AdminSite.index_title = "List of Data"
admin.AdminSite.site_title = "Book Recommender System"

class BookList(admin.ModelAdmin):
    list_display = ('id', 'title', 'publisher', 'publication_year')
    list_filter = ('publication_year', )
    search_fields = ('title', 'publisher')
    

admin.site.register(Book, BookList)