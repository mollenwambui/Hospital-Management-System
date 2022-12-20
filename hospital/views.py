from django.shortcuts import render
from .forms import CustomerRegistrationForm,AppointmentRegistrationForm
from .models import Customer,Appointment
# Create your views here.
def register_customer(request):
    if request.method=="POST":
       form=CustomerRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
    else:
           form=CustomerRegistrationForm()    
    return render (request,"register_customer.html",{"form":form})


def list_customer(request):
    customers=Customer.objects.all()
    return render(request,"customer_list.html",{"customers":customers})


def home(request):
    return render(request,"home.html")

def book_appointment(request):
    if request.method=="POST":
       form=AppointmentRegistrationForm(request.POST)
       if form.is_valid():
           form.save()
    else:
           form=AppointmentRegistrationForm   
    return render (request,"book_appointment.html",{"form":form})
