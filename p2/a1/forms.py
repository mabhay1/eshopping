from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile,Review,OrderUpdates
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget


    
class SignUpForm(UserCreationForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(),
        initial='+91'
    )



    class Meta:
        fields=('first_name','last_name','username','phone_number','email','password1','password2')
        model=UserProfile


class UpdateForm(forms.ModelForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(),
        initial='+91'
        )
    class Meta:
        model=UserProfile
        fields=['username','first_name','last_name','phone_number','email']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['rev','experience']
