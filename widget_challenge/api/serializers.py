from rest_framework import serializers
from .models import Finish, Size, Widget, Order, OrderItem

"""Serializer to map Model instances into JSON format."""
class FinishSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Finish
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Size
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')

class WidgetSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Widget
        fields = ('id', 'name', 'inventory', 'finish', 'size', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Widget
        fields = ('id', 'name', 'inventory', 'finish', 'size', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Widget
        fields = ('id', 'count', 'order', 'widget', 'date_created', 'date_modified')
        read_only_fields = ('id', 'date_created', 'date_modified')
