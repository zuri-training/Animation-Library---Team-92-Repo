from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'moov_app/index.html')

def errorPage(request):
    return render(request, "moov_app/error_page.html")
