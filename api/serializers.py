from rest_framework import serializers
from hospital.models import Customer,Appointment

class Customer_serializers(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=("first_name","middle_name","last_name","phone_number","age","gender","residential_address","company","insurance_id","occupation")
