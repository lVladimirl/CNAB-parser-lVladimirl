from django.shortcuts import render, get_object_or_404
from rest_framework import generics, views

from rest_framework.authentication import TokenAuthentication
from .models import Shop
from users.models import User

from .serializers import ShopViewSerializer, RegisterShopSerializer
from utils.permissions import isAdmin
import ipdb

class RegisterShopView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = Shop.objects.all()
    serializer_class = RegisterShopSerializer

    def perform_create(self, serializer):
        owner,r = User.objects.get_or_create(id=self.request.data['owner'])
        serializer.save(owner=owner)

class ListDetailUSerView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = Shop.objects.all()
    serializer_class = ShopViewSerializer

    lookup_field = "id"