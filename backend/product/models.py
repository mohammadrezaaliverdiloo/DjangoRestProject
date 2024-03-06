from django.db import models
from django.utils.translation  import gettext_lazy as _


class Category(models.Model):
    parenet = models.ForeignKey('self',related_name= 'parent',on_delete=models.CASCADE,verbose_name = _('parent'),null =True,blank=True)
    title = models.CharField(_('title'),max_length = 75)
    slug = models.SlugField(_('url'),unique= True)
    description = models.TextField(_('descrition'),blank = True)
    avatar = models.ImageField(_('image'),upload_to='categories/',)
    is_enable = models.BooleanField(_('status'),default= True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update_time'),auto_now=True)


    def __str__(self):
        return f'{self.title} - {self.slug}'
    
    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')



class Product(models.Model):
    category = models.ManyToManyField(Category,related_name= 'category',verbose_name = _('category'))
    title = models.CharField(_('title'),max_length = 255)
    slug = models.SlugField(_('url'),unique= True)
    description = models.TextField(_('descrition'),blank = True)
    avatar = models.ImageField(_('image'),upload_to='product/')
    is_enable = models.BooleanField(_('status'),default= True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update_time'),auto_now=True)


    def __str__(self):
        return f'{self.title} - {self.slug}'
    
    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        
    def get_category(self):
        return "-".join([p.title for p in self.category.all()])    
    
class File(models.Model):
    product = models.ForeignKey(Product,related_name= 'product',on_delete=models.CASCADE,verbose_name = _('product'))
    title = models.CharField(_('title'),max_length = 255)
    slug = models.SlugField(_('url'))
    file = models.FileField(_('file'),upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(_('status'),default= True)
    created_time = models.DateTimeField(_('created_time'),auto_now_add=True)
    update_time = models.DateTimeField(_('update_time'),auto_now=True)


    def __str__(self):
        return f'{self.title} - {self.slug}'
    
    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')