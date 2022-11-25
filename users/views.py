from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from utils.permissions import isAdmin
from .models import User
from .serializers import  UserSerializer

class CreateUserView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

class ListDetailUserView(generics.RetrieveAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserSerializer

    lookup_field = "id"