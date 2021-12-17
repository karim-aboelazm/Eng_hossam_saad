from django.urls import path
from .views import *
app_name = "My_Resume"

urlpatterns = [
    path('',home_page,name='home'),
    path('about/',about_page,name='about'),
    path('skills/',skills_page,name='skills'),
    path('my-services/',achievements_page,name='my_services'),
    path('my-portofolio/',portofolio_page,name='my_portofolio'),
    path('my-certifications/',certification_page,name='my_certifications'),
]
