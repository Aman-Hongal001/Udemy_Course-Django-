from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.

def index(request):
    return render(request,'index.html')

def form_name_view(request):
    form = forms.FormName()
    
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            print("Validation Success!")
            print("NAME : "+form.cleaned_data['name'])
            print("EMIAL : "+form.cleaned_data['email'])
            print("TEXT : "+form.cleaned_data['text'])
    
    return render(request,'formpage.html',{'form':form})