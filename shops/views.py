from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Shop, Category, SubCategory
from .serializers import ShopSerializers, CategorySerializers, SubCategorySerializers
from rest_framework import filters


# get, post, update, and delete
class ListAllShops(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class Category(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class SubCategory(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializers
