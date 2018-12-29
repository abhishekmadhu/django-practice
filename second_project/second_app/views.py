from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    myDict = {'username': "My name"}
    return render(request, 'second_app/index.html', context=myDict)

def help(request):
    myDict = {'content': "help content"}
    return render(request, 'second_app/help.html', context=myDict)