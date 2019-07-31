from django.contrib import admin
from article.models import Article, Comment, Tag


@admin.register(Article)
class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('id', 'author', 'message')

@admin.register(Tag)
class AdminTag(admin.ModelAdmin):
    list_display = ('id', 'name')

