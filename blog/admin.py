from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['heading', 'content', 'preview']
    list_filter = ['heading', 'create_at']
    ordering = ['create_at', 'heading']
