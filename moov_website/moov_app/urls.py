from django.urls import path
from . import views

app_name = 'moov_app'
urlpatterns = [
    path('', views.homepage, name='home'),
    path('error/', views.errorPage, name="error"),
    path('faqs/', views.FAQPage, name="faqs"),
]
