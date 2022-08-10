from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('error/', views.errorPage, name="error"),
    path('faqs/', views.FAQPage, name="faqs"),
    path('documentation', views.documentation, name='documentation'),
    path('t&c', views.terms, name='t&c'),



]
