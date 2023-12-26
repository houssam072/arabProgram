from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import Article

class NewArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','bio','tags','body','approved','message_body']
        