from django.shortcuts import render
from rest_framework import viewsets
from .models import Activity_Period
from .serializers import ActivitySerializer

class ActivityView(viewsets.ModelViewSet):
    queryset= Activity_Period.objects.all()# to pull all the data from database
    serializer_class= ActivitySerializer# will convert the data from database to json
