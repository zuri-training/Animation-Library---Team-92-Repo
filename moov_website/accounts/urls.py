from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login")

    
]
