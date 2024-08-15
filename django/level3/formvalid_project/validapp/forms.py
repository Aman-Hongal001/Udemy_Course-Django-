from django import forms

class FormData(forms.Form):
    name = forms.CharField(label="Your name", max_length=50, required=False)
    email = forms.EmailField(max_length=100)
    text = forms.CharField(widget=forms.Textarea)