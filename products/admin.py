from django.contrib import admin

from products.forms import ColorPickerForm
from products.models import *

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(SizeModel)
class SizeModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('created_at',)


@admin.register(ColorModel)
class ColorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')
    list_filter = ('created_at', 'name')
    form = ColorPickerForm


class ProductImageModelAdmin(admin.StackedInline):
    model = ProductImageModel


@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'short_description', 'long_description')
    list_filter = ('created_at', 'brand', 'categories', 'tags', 'colors', 'sizes')
    readonly_fields = ('real_price',)
    inlines = [ProductImageModelAdmin]
