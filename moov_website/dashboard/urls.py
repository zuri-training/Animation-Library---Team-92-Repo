from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('library/', views.library_view, name='library'),
    path('download_library', views.download_library, name='download'),
    path('Saved Animations/', views.saved_anime, name='saved_anime')
]
