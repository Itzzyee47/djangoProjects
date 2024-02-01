from django import forms
from .models import post,ur_details
from django.contrib.auth.models import User, auth


class regForm(forms.Form):
    user_name = forms.CharField(max_length=68,  widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    email = forms.EmailField( widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))
    password = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'placeholder': 'password', 'type':'password'})) 
    confrim_password = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'placeholder': 'Confirm password', 'type':'password'}))    
        
    def clean_un(self):
        data = self.cleaned_data['user_name']
        
        return data
        
    def clean_up(self):
        data = self.cleaned_data['password']
        
        return data
    
class logForm(forms.Form):
    user_name = forms.CharField(max_length=68,  widget=forms.TextInput(attrs={'placeholder': 'Enter your username'}))
    password = forms.CharField(max_length=20,  widget=forms.TextInput(attrs={'placeholder': '***********', 'type':'password'}))
    
    def clean_un(self):
        data = self.cleaned_data['user_name']
        
        return data
        
    def clean_up(self):
        data = self.cleaned_data['password']
        
        return data
    
class postForm(forms.ModelForm):
    
    class Meta:
        model = post
        fields = ['title','pic']
        
        
class eProfile(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password']
        
        
class eProfileD(forms.ModelForm):
    
    class Meta:
        model = ur_details
        fields = "__all__"
        