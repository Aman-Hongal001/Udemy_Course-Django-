from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import *


# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request,'index.html',context=date_dict)

def home(request):
    note = {'ind':"This is inside home function in views.py"}
    return render(request,'index.html',context=note)

