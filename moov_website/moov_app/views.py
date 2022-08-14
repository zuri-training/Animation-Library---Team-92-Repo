from django.shortcuts import render, redirect
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from .forms import *
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
def contactview(request):
    form = moov_contactForm()
    sender = settings.EMAIL_HOST_USER

    if request.method == 'POST':

        name = request.POST['name']
        email = request.POST['email']
        mes = request.POST['message']

        # mail_contact = 'your message is ' + mes + '\n Received from ' + email

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


def password_reset_request(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "templates/moov_app/password_reset_email.txt"
                    c = {
                        "email": 'user: email',
                        'domain': 'your-website-name.com',
                        'site_name': 'Website Name',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        'token': default_token_generator.make_token(user),
                        'protocol': 'https',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, '', [
                                  user.email], fail_silently=False)
                    except BadHeaderError:

                        return HttpResponse('Invalid header found.')

                    messages.success(
                        request, 'A message with reset password instructions has been sent to your inbox.')

            messages.error(request, 'An invalid email has been entered.')
    password_reset_form = PasswordResetForm()
    return render(request=request, template_name="templates/moov_app/password_reset.html", context={"password_reset_form": password_reset_form})


def password_reset(request):
    if request.method == 'POST':
        email = request.POST['email']

        mess = EmailMultiAlternatives(f'Welcome to Moov Animation', '')

        mess.attach_alternative("text/html")

        if mess.send():
            messages.add_message(request, messages.SUCCESS,
                                 f'Thank you {name} for your message')
        else:
            messages.add_message(request, messages.ERROR,
                                 'An error occured, please try again')

    return render(request, 'moov_app/contactus.html', {'moov_app': form})
