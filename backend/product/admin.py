from django.contrib import admin
from .models import File,Category,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable']#add parent an resolve foreignkey problem
    list_filter = ['is_enable','parent']
    search_fields = ['title']
    # filter_horizonta = ['parent']



class FileInLineAdmin(admin.StackedInline):
    model = File
    fields = ['title','file','is_enable']
    extra = 0


    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable']#add category and resolve M2M problem
    list_filter = ['is_enable']
    search_fields = ['title']
    # filter_horizontal = ['categories'] #resolve the problem
    
    inlines = [FileInLineAdmin]
    