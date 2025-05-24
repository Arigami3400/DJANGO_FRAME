from restframework import serializers
from .models import Product, ProductModel, Information


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'



class InformationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = '__all__'