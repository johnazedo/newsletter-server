from django.contrib import admin
from news.models import News, UserNews, Comment


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(UserNews)
class UserNewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass