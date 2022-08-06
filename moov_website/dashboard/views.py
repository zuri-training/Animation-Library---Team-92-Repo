from django.shortcuts import render

# Create your views here.


# library interface views

def library(request):
    return render(request, 'dashboard/library.html')


def saved_codes(request):
    return render(request, 'dashboard/saved.html')
