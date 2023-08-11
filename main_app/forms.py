from django.forms import ModelForm
from .models import *
#from .models import Feeding

#class FeedingForm(ModelForm):
  #class Meta:
    #model = Feeding
    #fields = ['date', 'meal']


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#class LoginForm(forms.Form):
    #username = forms.CharField(max_length=65)
    #password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1','password2'] 


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


#TAVY FORUM CODE 
class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"
 
class CreateInDiscussion(ModelForm):
    class Meta:
        model= Discussion
        fields = "__all__"