from django.urls import path,include
from .views import ProductListView

app_name = 'products'
urlpatterns = [
    path('products/',ProductListView.as_view(),name = 'product_list')
    

]
