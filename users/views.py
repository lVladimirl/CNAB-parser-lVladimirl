from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from utils.permissions import isAdmin
from .models import User
from .serializers import RegisterUserSerializer, UserDetailSerializer
from users.permissions import IsOwner, ListUsersValidation

class CreateUserView(generics.CreateAPIView, generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

class ListDetailUSerView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]

    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    lookup_field = "id"