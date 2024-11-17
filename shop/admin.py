from django.contrib import admin

from shop.models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent')
    ordering = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'slug', 'price', 'available', 'category', 'created_at')
    ordering = ('title',)
    list_filter = ('available', 'category', 'created_at')

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}