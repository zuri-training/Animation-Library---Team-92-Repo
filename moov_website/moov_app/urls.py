from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
<<<<<<< HEAD
    path('error/', views.errorPage, name="error"),
    path('faqs/', views.FAQPage, name="faqs"),
=======
    path('documentation', views.documentation,name='documentation')

>>>>>>> origin/GoddessOfWealth
]
