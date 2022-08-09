from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'moov_app/index.html')

def documentation(request):
    return render(request,'moov_app/library_Documentation.html' )

def homes(request):
    return render(request, 'moov_app/home.html')

