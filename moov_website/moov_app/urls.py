from django.urls import path, include
from .views import *

urlpatterns = [
    path('contact_us/', contactview, name='contact'),
]
