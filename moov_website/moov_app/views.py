
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from .forms import *
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def contactview(request):
    form = moov_contactForm()
    sender = settings.EMAIL_HOST_USER

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        mes = request.POST['message']

        mail_contact = 'your message is ' + mes + '\n Received from ' + email

        message = render_to_string(
            'templates/moov_app/sendmail.html', {'name': mes})
        mess = EmailMultiAlternatives(f'Welcome to Moov Animation', '', sender, [
                                      "teekaymartha@gmail.com"])

        mess.attach_alternative(message, "text/html")

        if mess.send():
            messages.add_message(request, messages.SUCCESS,
                                 f'Thank you {name} for your message')
        else:
            messages.add_message(request, messages.ERROR,
                                 'An error occured, please try again')

    return render(request, 'moov_app/contactus.html', {'moov_app': form})


def homepage(request):
    return render(request, 'moov_app/home.html')


def errorPage(request):
    return render(request, "moov_app/error_page.html")


def FAQPage(request):
    return render(request, "moov_app/faqs.html")


def documentation(request):
    return render(request, 'moov_app/library_documentation.html')


def terms(request):
    return render(request, 'moov_app/terms.html')


def privacy(request):
    return render(request, 'moov_app/privacy policy.html')


def error_404(request, exception):
    return render(request, 'moov_app/error_page.html')
