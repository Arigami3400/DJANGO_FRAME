from .models import import Product, ProductModel, Information
from .serializers import ProductSerializers, ProductModelSerializers, InformationSerializers
from rest_framework import viewsets


class InformationViewSet(viewsets.ModelViewSet):
    queryset = Information.objects.all()
    serializer_class = InformationSerializers


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductModelViewSet(viewsets.ModelViewSet):
    queryset = ProductModel.object.all()
    serializer_class = ProductModelSerializers
