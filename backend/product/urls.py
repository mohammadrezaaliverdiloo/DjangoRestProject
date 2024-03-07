from django.urls import path,include
from .views import( 
                   ProductListView,
                   ProducDeatailView,
                   CategoryListView,
                   CategoryDetailView,
                   FileListView,
                   FileDetailView,
                   )

app_name = 'products'
urlpatterns = [
    path('products/',ProductListView.as_view(),name = 'product_list'),
    path('products/<slug:slug>/',ProducDeatailView.as_view(),name = 'product_details'),
    path('category/',CategoryListView.as_view(),name = 'category_list'),
    path('category/<slug:slug>/',CategoryDetailView.as_view(),name = 'category_details'),
    path('files/',FileListView.as_view(),name = 'file_list'),
    path('files/<slug:slug>',FileDetailView.as_view(),name = 'file_detail'),
    
    #I have to create a url and view for get data from url like this 
    # path('products/<slug:product_slug>/files/',FileListView.as_view(),name = 'file_list'),
]
