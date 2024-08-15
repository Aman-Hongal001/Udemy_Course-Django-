from django import forms

class FormName(forms.Form):
    name = forms.CharField(label="Your name", max_length=100)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)