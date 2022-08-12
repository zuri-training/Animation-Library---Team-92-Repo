from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('success/', views.success, name='success'),
    path('forgot_password/', views.forgot_password, name='forgotPassword'),

    path('logout/', views.logout_view, name='logout'),


]
