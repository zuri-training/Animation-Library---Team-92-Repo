from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from accounts.forms import RegistrationForm


def register(request, *args, **kwargs):

    context = {}
    form = RegistrationsForm()
    if request.method == 'POST':
        form = RegsitrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)

# Create your views here.


def loginPage(request):
    page = 'login'

    # prevents users from entering the login page when already logged in.
    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = NewUser.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, 'Username OR Password does not exist.')

    context = {'page': page}
    return render(request, 'accounts/login.html', context)


def success(request):
    return render(request, 'accounts/successLogin.html')


def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')


def contact(request):
    return render(request, 'accounts/contact.html')
