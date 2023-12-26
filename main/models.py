from tkinter import CASCADE
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver







class Question(models.Model):
    auther = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length = 200, null = False)
    body = models.TextField(null = False)
    attach = models.ImageField(null= True,default='attach/11.JPG', blank=True, upload_to='attach/')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    


    def __str__(self):
        return self.title
    
    def get_response(self):
        return self.response.filter(parent = None)

class Response(models.Model):
    user = models.ForeignKey(User, null = False, on_delete = models.CASCADE)
    question = models.ForeignKey(Question, null = False, on_delete = models.CASCADE,related_name = 'response')
    parent = models.ForeignKey('self',null = True, blank = True, on_delete = models.CASCADE)
    body = models.TextField(null = False)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__ (self):
        return self.body
    
def image_upload(instance,filename):
    imagename, extention = filename.split('.')
    return 'profile/%s/%s.%s'%(instance.id,instance.id,extention)

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null= True,default='defult_profile_pic.jpg', blank=True, upload_to=image_upload)
    bio = models.TextField()
    
    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

