from rest_framework import serializers

from .models import File,Category,Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title','description','avatar',]

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['title','file']

class ProductSerializer(serializers.ModelSerializer):
    #category = serializers.StringRelatedField(many=True)
    category = CategorySerializer(many = True)
    
    class Meta:
        model = Product
        fields = ['title','description','avatar','category']
        
        
                
