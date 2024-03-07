from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import(
    File,Category,Product)
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
    
    # def get_objects(self,slug):
        
        
    
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
    # def get_objects(self,slug):

            
    
    def get(self,request,slug):
        try:
            category = Category.objects.filter(slug=slug)
        except Category.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)
        
        serializer  = CategorySerializer(category,many=True,context ={'request': request})
        return Response(serializer.data)      
  