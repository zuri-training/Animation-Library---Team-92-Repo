from django.urls import path
from . import views

# app_name = "dashboard"


urlpatterns = [
    path('tryout', views.dashboard, name='tryout'),
    path('savedAnimations', views.savedAnimations, name="saved_anime"),
    path('download_library', views.download_library, name='download'),


]
