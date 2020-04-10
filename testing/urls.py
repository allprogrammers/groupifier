from django.urls import path

from . import views

#here we associate the url in the app with the respective handler
#the one defined in the app views and give it a name


urlpatterns = [
    path('', views.index, name='index'),
]