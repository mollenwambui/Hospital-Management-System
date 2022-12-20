from django.urls import path,include
from rest_framework import routers
from .views import CustomerViewset

router=routers.DefaultRouter()
router.register(r"customers",CustomerViewset)

urlpatterns = [
    path("",include(router.urls)),
 
]
