<<<<<<< HEAD
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('error/', views.errorPage, name="error"),
    path('faqs/', views.FAQPage, name="faqs"),
    path('documentation', views.documentation, name='documentation'),
    path('t&c', views.terms, name='t&c'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact_us/', views.contactview, name='contact'),

=======
from django.urls import path , include
from .views import *
from . import views

urlpatterns = [
    path('contact_us/', contactview, name='contact'),
   path("password_reset", views.password_reset_request, name="password_reset")
   
>>>>>>> origin/toyin
]
