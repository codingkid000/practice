from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.my_data,name="my_data"),
    path("response/",views.my_response,name="my_response"),
    path("getResponse/",views.getResponse,name="getResponse"),
    
    
]
