from django.urls import path
from .views import register_customer,list_customer,home,book_appointment


urlpatterns = [
    path("register/",register_customer,name="registration"),
    path("customer/",list_customer,name="customer"),
    path("home/",home,name="home"),
    path("appointment/",book_appointment,name="appointment")
]   
