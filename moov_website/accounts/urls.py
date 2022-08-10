from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('successLog/', views.successReg, name='successReg'),
    path('forgot_password/', views.forgot_password, name='forgotPassword'),
    path('contact/', views.contact, name='contact'),
    path('privacy/', views.privacy, name='privacy')

]
