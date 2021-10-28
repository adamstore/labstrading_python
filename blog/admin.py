from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'email', 'date_posted', 'status')
    list_filter = ('status', 'date_posted')
    search_fields = ('name', 'body')