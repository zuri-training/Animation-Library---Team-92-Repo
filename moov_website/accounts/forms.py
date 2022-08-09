from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from accounts.models import NewUser


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=254, help_text='Required. Add a valid email address.')

    class Meta:
        model = NewUser
        fields = ('user_name', 'email', 'password')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = NewUser.objects.exclude(
                pk=self.instance.pk).get(email=email)
        except NewUser.DoesNotExist:
            return email
        raise forms.ValidationError('Email "%s" is already in use.' % account)

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            account = NewUser.objects.exclude(
                pk=self.instance.pk).get(user_name=user_name)
        except NewUser.DoesNotExist:
            return username
        raise forms.ValidationError(
            'Username "%s" is already in use.' % username)


# class UserLogin(forms.ModelForm):
#     password = forms.CharField(label="password", widget=forms.PasswordInput)

#     class Meta:
#         model = NewUser
#         fields = ("email", "password")

#         def clean(self):
#             if self.is_valid():
#                 email = self.cleaned_data['email']
#                 password = self.cleaned_data['password']

        # if not authenticate(email=email, password=password):
        #     raise forms.ValidationError("invalid Login")
