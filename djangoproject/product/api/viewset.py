from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from django_filters import rest_framework as filters
from product.models import Product, Category

from product.api.serializers import UserSerializer, CategorySerializer, ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductsFilter(filters.FilterSet):
    price = filters.CharFilter(lookup_expr='lte')
    class Meta:
        model = Product
        fields = ('category', 'price', 'stock', 'deal')


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    filter_class = ProductsFilter
    permission_classes = [permissions.IsAuthenticated]


