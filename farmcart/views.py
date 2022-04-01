# from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin ,RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from .serializers import ProductSerializer
from .models import Product
# from django.conf import settings
# Create your views here.

# def index(request):
#     print("cartlist - views --", settings.STATICFILES_DIR)
#     return HttpResponse("ok")

# class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet):
#     # print("django check", settings.STATICFILES_DIR)
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer


class ProductViewSet(ListModelMixin,RetrieveModelMixin,GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
