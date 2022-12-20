from django import forms
from .models import Customer,Appointment

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"


class AppointmentRegistrationForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"
