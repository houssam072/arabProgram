from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from tinymce import models as tinymcs_models

class Article(models.Model):
    auther = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length= 200, null = False)
    bio = models.CharField(max_length = 450, null = False)
    tags = TaggableManager()
    body = RichTextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    approved = models.BooleanField('approved', default = 'False')
    show = models.BooleanField('show', default = 'False')
    message_body = models.TextField(max_length=200, null = False,blank=True)


    
    def __str__(self):
        return self.title



