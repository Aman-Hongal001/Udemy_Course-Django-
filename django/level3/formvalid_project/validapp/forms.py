from typing import Any
from django import forms
from django.core import validators


# custom validation function 
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEED TO START WITH Z")

class FormData(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    # name = forms.CharField()
    email = forms.EmailField(max_length=100)
    verify_email = forms.EmailField(label='Enter your Email Again')
    text = forms.CharField(widget=forms.Textarea)
    
    botcatcher = forms.ChoiceField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
    
    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['verify_email']
        
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAIL MATCHES")