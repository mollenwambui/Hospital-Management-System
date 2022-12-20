from django.db import models
from django.utils import timezone



# Create your models here.

class Customer(models.Model):
    first_name=models.CharField(max_length=15)
    middle_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15)
    # date_of_birth=models.DateField(null=True)
    phone_number=models.CharField(max_length=10,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    GENDER_CHOICE = (("Male","Male"),("Female","Female"))
    gender=models.CharField(max_length=12,choices=GENDER_CHOICE,null=True)
    residential_address=models.CharField(max_length=20,null=True)
    company=models.CharField(max_length=60,null=True)
    insurance_id=models.CharField(max_length=20,null=True)
    occupation=models.CharField(max_length=10,null=True)


class Appointment(models.Model)  :
    Doctors_Choice=(("Mollen","Mollen"),("Joy","Joy"),("Mark","Mark"))
    Doctors=models.CharField(max_length=20,choices=Doctors_Choice,null=True)
    Appointment_Choice=(("Check-up","Check-up"),("Weekly Appointments","Weekly Appointments"),("Feeling unwell","Feeling unwell"))
    Appointment=models.CharField(max_length=20,choices=Appointment_Choice,null=True)
    Select_Time=models.TimeField(null=True)
    
