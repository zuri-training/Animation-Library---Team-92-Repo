from django.shortcuts import render

# Create your views here.


def homepage(request):
    return render(request, 'moov_app/index.html')

<<<<<<< HEAD
def errorPage(request):
    return render(request, "moov_app/error_page.html")

def FAQPage(request):
    return render(request, "moov_app/faqs.html")
=======
def documentation(request):
    return render(request,'moov_app/library_documentation.html')

>>>>>>> origin/GoddessOfWealth
