from django.shortcuts import render

from rest_framework import generics
from .serializers import *
from .models import *

# Views handling Finish class
class FinishCreateView(generics.ListCreateAPIView):
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

    def perform_create(self, serializer):
        serializer.save()

class FinishDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

# Views handling Size class
class SizeCreateView(generics.ListCreateAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def perform_create(self, serializer):
        serializer.save()

class SizeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

# Views handling Category class
class CategoryCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save()

# Views handling Widget class
class WidgetCreateView(generics.ListCreateAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

    def perform_create(self, serializer):
        serializer.save()

class WidgetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

# Views handling Order class
class OrderCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Views handling Order class
class OrderItemCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    def perform_create(self, serializer):
        serializer.save()

class OrderItemDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer