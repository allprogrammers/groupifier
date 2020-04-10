from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#define the handler for the page use request as a parameter
# the handler should return a HttpResponse after the processing
#the name can be anything you want but it should be the same as the one mentioned in the urls

#because the returned response is a httpresponse it can be any standard http response as studied in computer networks
#but the full understanding will come with practice and experimentation so just google for now

def index(request):
    return HttpResponse("hello world")