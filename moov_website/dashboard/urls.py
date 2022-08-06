from django.urls import path
from . import views

urlpatterns = [
    path("library", views.library, name='library'),
    path("saved_codes", views.saved_codes, name="saved_codes")
]
