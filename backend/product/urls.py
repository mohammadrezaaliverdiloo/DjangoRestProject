from django.urls import path,include
from .views import ProductListView,ProducDeatailView

app_name = 'products'
urlpatterns = [
    path('products/',ProductListView.as_view(),name = 'product_list'),
    path('products/<slug:slug>/',ProducDeatailView.as_view(),name = 'product_details'),
    
]
