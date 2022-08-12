from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
urlpatterns = [

    path('register/', views.register, name='register'),
    path('login/', views.loginPage, name='login'),
    path('success/', views.success, name='success'),
    path('forgot_password/', views.forgot_password, name='forgotPassword'),

    path('logout/', views.logout_view, name='logout'),



=======
from django.conf.urls.static import static


urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login")

    
>>>>>>> origin/toyin
]
