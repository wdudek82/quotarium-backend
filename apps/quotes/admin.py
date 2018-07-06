from django.contrib import admin
from .models import Author, Quote


class QuoteInline(admin.TabularInline):
    model = Quote
    extra = 1


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'text', 'created_at', 'updated_at']
    search_fields = ['author', 'text']


@admin.register(Author)
class Author(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_filter = ['first_name', 'last_name']
    inlines = [QuoteInline]
