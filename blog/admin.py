from django.contrib import admin
from blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'is_public',)
    list_filter = ('is_public',)
    search_fields = ('title', 'content', 'slug',)
