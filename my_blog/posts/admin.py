from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = []

