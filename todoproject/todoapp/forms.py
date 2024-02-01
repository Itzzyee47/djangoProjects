from django import forms
from .models import task


class taskform(forms.ModelForm):
    class Meta:
        model = task
        fields = ["title", "discription", "set_date"]
    
    def clean_title(self):
        title = self.cleaned_data['title']
        # description = self.cleaned_data['description']
        # set_date = self.cleaned_data['set_date']
        
        if title == '':
            raise forms.ValidationError("title must be filled")
        # elif set_date != :
            
        return title
    
    