from django.shortcuts import render

from rest_framework import generics
from .serializers import *
from .models import *

# Views handling Finish class
class FinishCreateView(generics.ListCreateAPIView):
    serializer_class = FinishSerializer

    def get_queryset(self):
        queryset = Finish.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        sort = self.request.query_params.get('sort', None)
        desc = "-" if (self.request.query_params.get('desc', None)) else ""
        if sort is not None:
            queryset = queryset.order_by(desc + sort)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

class FinishDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

# Views handling Size class
class SizeCreateView(generics.ListCreateAPIView):
    serializer_class = SizeSerializer

    def get_queryset(self):
        queryset = Size.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        sort = self.request.query_params.get('sort', None)
        desc = "-" if (self.request.query_params.get('desc', None)) else ""
        if sort is not None:
            queryset = queryset.order_by(desc + sort)
        return queryset

    def perform_create(self, serializer):
        serializer.save()

class SizeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

# Views handling Category class
class CategoryCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        sort = self.request.query_params.get('sort', None)
        desc = "-" if (self.request.query_params.get('desc', None)) else ""
        if sort is not None:
            queryset = queryset.order_by(desc + sort)
        return queryset

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

    def get_queryset(self):
        queryset = Widget.objects.all()
        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        sort = self.request.query_params.get('sort', None)
        desc = "-" if (self.request.query_params.get('desc', None)) else ""
        if sort is not None:
            queryset = queryset.order_by(desc + sort)
        return queryset

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