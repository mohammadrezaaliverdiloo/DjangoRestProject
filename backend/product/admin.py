from django.contrib import admin
from .models import File,Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','parenet']
    list_filter = ['is_enable','parenet']
    search_fields = ['title']
    filter_horizonta = ['parenet']


class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','is_enable','slug','file_type']
    extra = 0

    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','get_category']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['category']
    
    inlines = [FileInLineAdmin]
    