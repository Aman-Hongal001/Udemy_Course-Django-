from django.shortcuts import render
# from django.http import HttpResponse
# from modelformapp.models import User
from modelformapp.forms import NewUserForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def users(request):
    
    form = NewUserForm()
    
    if request.method == "POST":
        form = NewUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            return index(request)
        else:
            print('ERROR FROM INVALID')
    
    return render(request,'users.html',{'form':form})

