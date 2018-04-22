from rest_framework import serializers
from .models import *

"""Serializer to map Model instances into JSON format."""
class FinishSerializer(serializers.ModelSerializer):
    """Meta class to map serializer's fields with the model fields."""
    class Meta:
        model = Finish
        fields = '__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')

class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = '__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('id', 'date_created', 'date_modified')
