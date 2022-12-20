from django.shortcuts import render
from rest_framework import viewsets
from hospital.models import Customer,Appointment
from .serializers import Customer_serializers

# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=Customer_serializers