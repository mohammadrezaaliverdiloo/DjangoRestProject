from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



''''
I have to create product view for get files with 
url  slu from '/product/<slug:slug>/files/<slug:slug for files>
and iterate on file from category side

'''


from .models import(
    File,Category,Product
    )
from .serializer import (
    ProductSerializer,
    CategorySerializer,
    FileSerializer
)

class ProductListView(APIView):
    
    def get(self,request):
        products = Product.objects.all()
        serializer  = ProductSerializer(products,many=True,context ={'request': request})
        return Response(serializer.data)


    
class ProducDeatailView(APIView):
              
    def get(self,request,slug):
        try:
            product = Product.objects.filter(slug=slug)
        except Product.DoesNotExist:
            status = status.HTTP_404_NOT_FOUND
            return Response(status)        
        
        serializer  = ProductSerializer(product,many=True,context ={'request': request})
        return Response(serializer.data)    

    
class CategoryListView(APIView):
   
   def get(self,request):
      category=Category.objects.all()
      serializer=CategorySerializer(category,many = True)
      print("hello evrybody")
      return Response(serializer.data)
  
  
  
class CategoryDetailView(APIView):
 
    def get(self,request,slug):
        try:
            category = Category.objects.filter(slug=slug)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer  = CategorySerializer(category,many=True,context ={'request': request})
        return Response(serializer.data)  
    
    
class FileListView(APIView):
    
    def get(self,request): # add ,slug and resolve the problem beacuase I have to create 
        try:
            files = File.objects.all()
            # files = File.objects.filter(slug = slug) I have to get file for every product one by one 
        except File.DoesNotExist:
            return Response (status = status.HTTP_404_NOT_FOUND)
        
        serializer = FileSerializer(files,many=True,context = {'request':request})        
        return Response(serializer.data)    
    
    
    
  
class FileDetailView(APIView):
 
    def get(self,request,slug): #add product_slug
        try:
            files = File.objects.filter(slug=slug) # add an d resolve the problem product_slug=product_slug
        except File.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer  = FileSerializer(files,many=True,context ={'request': request})
        return Response(serializer.data)  
    
      
  