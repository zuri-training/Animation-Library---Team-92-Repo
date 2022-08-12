from django.urls import path , include
from .views import *
from . import views

urlpatterns = [
    path('contact_us/', contactview, name='contact'),
   path("password_reset", views.password_reset_request, name="password_reset")
   
]
