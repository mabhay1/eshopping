from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import UserProfile,Review,OrderUpdates,Product
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
class ProductCreateForm(forms.ModelForm):
    class Meta():
        model=Product
        fields=['category','name','image','price','description']
        

    
class SignUpForm(UserCreationForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(),
        initial='+91'
    )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and UserProfile.objects.filter(email=email).exclude(username=username).exists():
            raise forms.ValidationError(u'this email is already taken use different email')
        return email



    class Meta:
        fields=('first_name','last_name','username','phone_number','email','password1','password2','role')
        model=UserProfile


class UpdateForm(forms.ModelForm):
    phone_number=PhoneNumberField(
        widget=PhoneNumberPrefixWidget(),
        initial='+91'
        )
    class Meta:
        model=UserProfile
        fields=['username','first_name','last_name','phone_number','email','role']

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields=['rev','experience']
