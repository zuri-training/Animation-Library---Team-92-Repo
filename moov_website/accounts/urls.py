from unicodedata import name
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('successLogin/', views.successLog, name="SuccessLogin"),
    path('forgot password/', views.forgot_password, name="forgot password")
    


]
