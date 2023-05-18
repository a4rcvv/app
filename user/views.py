from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, permissions
from .models import User
from django.db import transaction
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.response import Response


class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class RetrieveUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except User.DoesNotExist:
            raise Http404


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except User.DoesNotExist:
            raise Http404
        
class DestroyUserView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get_object(self):
        try:
            instance = self.queryset.get(email=self.request.user)
            return instance
        except User.DoesNotExist:
            raise Http404
