from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name='index'),
    path("other/",views.other,name='other'),
    path("relative/",views.relative,name='relative')
]

#template taging starts here
app_name = 'basic_app'
