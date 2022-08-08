from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.library_view, name='library')
]
