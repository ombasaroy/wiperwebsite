from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at', 'featured_image_preview')
    prepopulated_fields = {'slug': ('title',)}

    def featured_image_preview(self, obj):
        if obj.featured_image:
            return f'<img src="{obj.featured_image.url}" width="50" height="50"/>'
        return ""

    featured_image_preview.allow_tags = True
    featured_image_preview.short_description = "Featured Image"


admin.site.register(Post, PostAdmin)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Fields to show in the admin list
    search_fields = ('name',)  # Enable search by name
    prepopulated_fields = {"slug": ("name",)}  # Auto-generate slug from name
    ordering = ('-created_at',)  # Order by newest first


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    prepopulated_fields = {"slug": ("name",)}


@admin.register(PDFDocument)
class PDFDocumentAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'file')


@admin.register(PDFCategory)
class PDFCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')