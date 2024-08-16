from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':"Hello Index by Dict", 'number':100}
    return render(request,'index.html',context_dict)

def other(request):
    return render(request,'other.html')

def relative(request):
    return render(request,'rel_url_template.html')