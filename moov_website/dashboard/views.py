from django.shortcuts import render

# Create your views here.


def library_view(request):
    return render(request, 'dashboard/library.html')
