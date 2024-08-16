from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'rel_url_template.html')