from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


# Create your views here.
class UserView(generics.ListAPIView):
    model = User
    serializer_class = UserSerializer
    queryset = User.objects.all()
