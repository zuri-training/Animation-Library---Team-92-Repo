from django.shortcuts import render

# Create your views here.


def library_view(request):
    return render(request, 'dashboard/library.html')

# saved codes view


def saved_codes(request):
    code = request.GET['codes']
    context = {'code': code}

    return render(request, 'dashboard/saved.html', context)
