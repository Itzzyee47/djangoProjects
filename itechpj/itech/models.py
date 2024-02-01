from django.db import models
from django.conf import settings

# Create your models here...
class ur_details(models.Model):
    
    s = (
        ('Female',
        'female'),
        ('Male',
        'male'),
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,editable=False,
    )
    proPic = models.ImageField(upload_to='proPics', blank=True, default=None)
    coverPhoto = models.ImageField(upload_to='covers', blank=True,  default=None)
    DOB = models.DateField( blank=True)
    discription = models.CharField(max_length=200, blank=True)
    location = models.CharField(max_length=100,  blank=True)
    sex = models.CharField(choices=s, max_length=7, blank=True)
    
    
class post(models.Model):
    aurthor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.TextField(max_length=500, default='',blank=True)
    pic = models.ImageField(upload_to='post',blank=True, null=True, default=None)
    
    
class like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,editable=False,
    )
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class comment(models.Model):
    user = models.ForeignKey(
         settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,editable=False,
    )
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
