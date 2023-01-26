from pyexpat import model
from rest_framework import serializers
from Allmodels.models import Categories, Order, Product


class ProductSerializer(serializers.ModelSerializer):
    createdAt = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ("productName", "productPrice",
                  "description", "status", "category", "image", "createdAt", "owner")


class ListProductSerializer(serializers.ModelSerializer):
    createdAt = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ("id", "productName", "productPrice",
                  "description", "status", "category", "image", "createdAt", "owner")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ("catName",)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "productId", "amount",
                  "quantity", "payment", "orderComplete")


class GetOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ("owner", "productId", "amount",
                  "quantity", "payment", "orderComplete")
