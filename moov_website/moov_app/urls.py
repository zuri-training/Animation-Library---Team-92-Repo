from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('documentation',views.documentation, name='documentation'),
    path('homes', views.homes, name='homes')

]

