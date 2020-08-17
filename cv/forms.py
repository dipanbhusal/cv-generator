from django import forms 

class cvForm(forms.Form):
    fullName = forms.CharField( widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput()) 
    github  = forms.CharField(label="https://github.com/username")
    
    website = forms.CharField()
    phone = forms.CharField(widget=forms.NumberInput()) 
    education = forms.CharField(widget=forms.Textarea())  