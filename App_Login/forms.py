from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from App_Login.models import UserProfile

class UserRegistrationForm(UserCreationForm):
    first_name=forms.CharField( required=True)
    last_name=forms.CharField( required=True)
    email = forms.EmailField(required=True,help_text = "<ul><li>Your password can&#39;t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can&#39;t be a commonly used password.</li><li>Your password can&#39;t be entirely numeric.</li></ul>")

    class Meta:
        model=User
        fields=('first_name','last_name','email','username','password1','password2')

class UserProfileUpdate(UserChangeForm):
    first_name=forms.CharField()
    last_name=forms.CharField()
    email=forms.CharField()

    class Meta:
        model=User
        fields=('first_name','last_name','email')

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields =('profile_pic',)

    