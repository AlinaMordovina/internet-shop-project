from django.contrib import admin
from catalog.models import Product, Category, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'content', 'preview', 'is_public',)
    list_filter = ('is_public',)
    search_fields = ('title', 'content', 'slug',)
