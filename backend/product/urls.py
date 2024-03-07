from django.urls import path,include
from .views import( 
                   ProductListView,
                   ProducDeatailView,
                   CategoryListView,
                   CategoryDetailView,
                   )

app_name = 'products'
urlpatterns = [
    path('products/',ProductListView.as_view(),name = 'product_list'),
    path('products/<slug:slug>/',ProducDeatailView.as_view(),name = 'product_details'),
    path('category/',CategoryListView.as_view(),name = 'category_list'),
    path('category/<slug:slug>/',CategoryDetailView.as_view(),name = 'category_details'),
    
]
