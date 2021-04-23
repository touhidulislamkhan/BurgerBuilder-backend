from django.shortcuts import render
from rest_framework import viewsets, permissions

from .serializers import UserProfileSerializer, OrderSerializer
from .models import UserProfile, Order

# Create your views here.


class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()


class OrderViewset(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    # queryset = Order.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        queryset = Order.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(user__id=id)

        return queryset
