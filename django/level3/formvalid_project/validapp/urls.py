from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name='index'),
    path("formpage/",views.form_deatils,name='form_details')
]
