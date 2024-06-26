from rest_framework import serializers
from . import models


class VendorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address']
        depth = 1


class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['id', 'user', 'address']
        depth = 1


class ProductListSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title',
                  'detail', 'price', 'product_ratings']
        depth = 1


class ProductDetailSerializer(serializers.ModelSerializer):
    product_ratings = serializers.StringRelatedField(
        many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ['id', 'category', 'vendor', 'title',
                  'detail', 'price', 'product_ratings']
        depth = 1


class CustomerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'mobile']
        depth = 1


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'mobile']
        depth = 1


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ['id', 'customer']
        depth = 1


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['id', 'order', 'product']
        depth = 1


class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomerAddress
        fields = ['id', 'customer', 'address', 'default_address']
        depth = 1


class ProductRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductRating
        fields = ['id', 'customer', 'product', 'rating', 'reviews', 'add_time']
        depth = 1
