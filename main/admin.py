from django.contrib import admin
from .models import *


# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'publication_year', 'create_at', 'update_at')
    list_filter = ('author', 'publication_year', 'create_at', 'update_at')


admin.site.register(Book, BookAdmin)
