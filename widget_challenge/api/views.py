from django.shortcuts import render

from rest_framework import generics
from .serializers import FinishSerializer, SizeSerializer, WidgetSerializer, OrderSerializer, OrderItemSerializer
from .models import Finish, Size, Widget, Order, OrderItem

class CreateView(generics.ListCreateAPIView):
    """This class defines the create behavior of our REST API."""
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT, and DELETE requests."""
    queryset = Finish.objects.all()
    serializer_class = FinishSerializer
