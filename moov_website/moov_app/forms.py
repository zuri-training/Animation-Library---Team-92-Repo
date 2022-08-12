
from django import forms

class moov_contactForm(forms.Form):
    name = forms.CharField(max_length=255, label='Full Name', widget = forms.TextInput(attrs={'class': 'contact_form', 
    'placeholder': 'Enter Full'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'contact_form', 'placeholder': 'example@gmail.com', 'required': 'True'}))
    message = forms.CharField(max_length =1000, label='message', widget= forms.Textarea(attrs={'class': 'contact_form',
     'placeholder': 'Enter your Message', 'rows': 4}))

class moov_forgetForm(forms.Form):
    username = forms.CharField(max_length=255, label='Username', widget = forms.TextInput(attrs={'class': 'forget_form', 'placeholder': 'Enter Username'}))
    email = forms.EmailField(widget= forms.EmailInput(attrs={'class': 'contact_form', 'placeholder': 'example@gmail.com', 'required': 'True'}))


class moov_changeForm(forms.Form):
    new_password = forms.CharField(max_length=255, label='Full Name', widget = forms.TextInput(attrs={'class': 'contact_form', 
    'placeholder': 'Enter Full'}))
    confirm_password = forms.CharField(max_length=255, label='Full Name', widget = forms.TextInput(attrs={'class': 'contact_form', 
    'placeholder': 'Enter Full'}))