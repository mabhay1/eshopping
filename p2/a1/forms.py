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
    # def clean(self):
    #     status=False
    #     cleaned_data=super().clean()    
    #     user1=cleaned_data.get("user")
    #     print(user1)
    #     print(type(user1))
    #     product1=cleaned_data.get("product")
    #     a=UserProfile.objects.get(username=user1).order_set.filter(product__name=product1)
    #     for i in a:
    #         if i.orders.all().latest("updates_date"):
    #             status=True
    #             break
    #     if status:
    #         pass
    #     else:
    #          raise forms.ValidationError(
    #                 "you have not purchased  this product"
    #             )    

