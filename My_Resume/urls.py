from django.urls import path
from .views import *
app_name = "My_Resume"

urlpatterns = [
    path('',home_page,name='home'),
]