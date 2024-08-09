from django.shortcuts import render
from level2_app.models import User

# Create your views here.
def index(request):
    divert_dict = {'divert':"Go to /users to see the list information!"}
    return render(request,'index.html',context=divert_dict)

def user(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'user':user_list}
    return render(request,'user.html',context=user_dict)
