from django.urls import path, include
from . import views

app_name = 'moov_app'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('error/', views.errorPage, name="error"),
    path('faqs/', views.FAQPage, name="faqs"),
    path('documentation', views.documentation, name='documentation'),
    path('t&c', views.terms, name='t&c'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact_us/', views.contactview, name='contact'),

]
