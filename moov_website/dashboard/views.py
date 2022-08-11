from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


@login_required(login_url="/account/login")
def library_view(request):
    return render(request, 'dashboard/library.html')

# saved codes view


@login_required(login_url="/account/login")
def saved_anime(request):
    return render(request, 'dashboard/saved.html')


@login_required(login_url="/account/login")
def download_library(request):
    return render(request, 'dashboard/download.html')
