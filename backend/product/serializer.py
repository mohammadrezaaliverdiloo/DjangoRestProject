from rest_framework import serializers

from .models import File,Category,Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['slug','title','description','avatar']

class FileSerializer(serializers.HyperlinkedModelSerializer):
    file_type =serializers.SerializerMethodField()
    
    
    class Meta:
        model = File
        fields = ['slug','title','file','file_type']#add ,'file_set'

    def get_file_type (self,obj):
        return obj.get_file_type_display()
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    #category = serializers.StringRelatedField(many=True)
    category = CategorySerializer(many = True)
    files = FileSerializer(many = True)

    
    class Meta:
        model = Product
        fields = ['slug','title','description','avatar','category','files'] # when I add file_set,give a error with this content attribiute not exists

    
    # create a custom attribute
    # foo = serializers.SerializerMethodField()       
    # def get_foo (self,obj):
    #     return obj.id
                
