from django.contrib import admin
from .models import Customer,Appointment
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","middle_name","last_name" ,"phone_number","age","gender","residential_address","company","insurance_id","occupation",)
    search_fields = ("first_name","last_name",)
admin.site.register(Customer,CustomerAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("Doctors","Appointment","Select_Time")
    search_fields = ("Doctors",)
admin.site.register(Appointment,AppointmentAdmin)
