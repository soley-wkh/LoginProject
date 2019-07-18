from django.contrib import admin
from Article.models import *


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'date', 'description']
    list_display_links = ['title']
    # list_editable = ['author']
    list_per_page = 10


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender', 'age']
    list_per_page = 10


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


# Register your models here.


admin.site.register(Article, ArticleAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Type, TypeAdmin)
# admin.site.register(Article)
# admin.site.register(Author)
# admin.site.register(Type)
