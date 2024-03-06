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
        serializer  = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
class CategoryListView(APIView):
   
   def get(self,request):
      category=Category.objects.all()
      serializer=CategorySerializer(category,many = True)
      return Response(serializer.data)
  