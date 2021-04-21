from django.shortcuts import render
from rest_framework import viewsets

from .serializers import UserProfileSerializer, OrderSerializer
from .models import UserProfile, Order

# Create your views here.


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
