from rest_framework import serializers

from .models import File,Category,Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['slug','title','description','avatar']

class FileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = File
        fields = ['title','file']#add ,'file_set'

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #category = serializers.StringRelatedField(many=True)
    category = CategorySerializer(many = True)
    product = FileSerializer(many = True)

    
    class Meta:
        model = Product
        fields = ['slug','title','description','avatar','category','product'] # when I add file_set,give a error with this content attribiute not exists

    
    # create a custom attribute
    # foo = serializers.SerializerMethodField()       
    # def get_foo (self,obj):
    #     return obj.id
                
