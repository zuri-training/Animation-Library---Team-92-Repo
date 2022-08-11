from django.shortcuts import render

# Create your views here.


def library_view(request):
    return render(request, 'dashboard/library.html')

# saved codes view


def saved_codes(request):
    return render(request, 'dashboard/saved.html')


def download_library(request):
    return render(request, 'dashboard/download.html')
