
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def contactview(request):
    form = moov_contactForm()
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
       
        
        
        
        messages.add_message(request, messages.SUCCESS, "Thank you for contacting us")
        return redirect('contact')
       

    return render(request, "moov_app/contactus.html", {'moov_app': form})



