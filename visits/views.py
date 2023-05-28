from django.shortcuts import render
from rest_framework import generics
from .models import Visits
from .serializers import VisitsSerializer

class VisitsView(generics.CreateAPIView):
    model = Visits
    serializer_class = VisitsSerializer
    queryset = Visits.objects.all()

