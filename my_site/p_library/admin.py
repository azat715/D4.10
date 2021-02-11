from django.contrib import admin

# Register your models here.

from p_library.models import Book, Author, Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'copy_count', 'publisher')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass
    # fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    pass