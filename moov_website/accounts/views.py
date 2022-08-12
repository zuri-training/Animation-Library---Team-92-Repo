from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from accounts.forms import RegistrationForm


def register(request, *args, **kwargs):

    # user = request.user
    # if user.is_authenticated:
    # 	return HttpResponse("You are already authenticated as " + str(user.email))

    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email').lower()
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('login')
        else:
            context['registration_form'] = form

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


def logout_view(request):
    logout(request)
    return redirect('home')


def success(request):
    return render(request, 'accounts/successLogin.html')


def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')

