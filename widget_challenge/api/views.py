from django.shortcuts import render

from rest_framework import generics
from .serializers import FinishSerializer, SizeSerializer, WidgetSerializer, OrderSerializer, OrderItemSerializer
from .models import Finish, Size, Widget, Order, OrderItem

class FinishCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our REST API."""
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class FinishDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

class SizeCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our REST API."""
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class SizeDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""
    queryset = Size.objects.all()
    serializer_class = SizeSerializer

class WidgetCreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our REST API."""
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class WidgetDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""
    queryset = Widget.objects.all()
    serializer_class = WidgetSerializer
