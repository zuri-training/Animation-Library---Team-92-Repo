from django.shortcuts import render
from .forms import RegistrationForm
from .models import NewUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect


# Create your views here.


def register(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username, password=password)

            return redirect('login')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, "accounts/register.html", context)



def loginPage(request):
    page = 'login'

    # prevents users from entering the login page when already logged in.
    if request.user.is_authenticated:
        return redirect('home')

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
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password does not exist.')

    context = {'page': page}
    return render(request, 'accounts/login.html', context)


def successReg(request):
    return render(request, 'accounts/successLogin.html')


def forgot_password(request):
    return render(request, 'accounts/forgot_password.html')


def contact(request):
    return render(request, 'accounts/contact.html')


def privacy(request):
    return render(request, 'accounts/privacy policy.html')

