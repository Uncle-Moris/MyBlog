from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title']
    date_hierarchy = 'publish'
    list_filter = ['title']
    prepopulated_fields = {"slug": ("title",)}
