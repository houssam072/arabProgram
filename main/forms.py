from dataclasses import fields
from logging import PlaceHolder
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Question,Response,Profile


class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        widgets = {
            'email':forms.EmailInput(attrs = {
                'required' : True,
                'placeholder' : 'Email@gmail.com',
                'autofocus' : True
            }),
            
            'username':forms.TextInput(attrs = {
                'required' : True,
                'placeholder' : 'Full Name'
            })
        }
        def __init__(self, *args, **kwargs):
            super(RegisterUserForms, self).__init__(*args, **kwargs)
            self.fields['password1'].widget.attrs={'placeholder': 'Password from numbers and letters of the Latin alphabet'}
            self.fields['password2'].widget.attrs={'placeholder': 'Password confirmation'}

class LoginUserForms(AuthenticationForm):
    class Meta:
        fields = '__all__'

class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'attach']
        widgets = {
            'title' : forms.TextInput(attrs= {
                'placeholder' : 'enter the title of your Question',
                'autofocus' : True,
                'name' : 'title'
            }),
            
            'body' : forms.Textarea(attrs= {
                'placeholder' : 'enter the body of your Question',
                'name' : 'body'
            })
        }

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets = {
            'body' : forms.TextInput(attrs= {
                'placeholder' : 'enter your Answer here...',
                'name' : 'body'
            })
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name', 'last_name' ]
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'placeholder': 'Email'
                }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'الاسم الأول'
                }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'الاسم الأخير'
                })
        }
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic','bio']
        widgets = {
            
            'profile_pic': forms.FileInput(attrs={
                'required' : True,
                }),
            'bio': forms.Textarea(attrs={
                'class': "form-control", 
                'style': 'height :100px;',
                })

        }
     