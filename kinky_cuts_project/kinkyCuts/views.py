from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {}
    return render(request, 'kinkyCuts/index.html', context_dict)

def about(request):
    context_dict = {}
    return render(request, 'kinkyCuts/about.html', context_dict)

def explore(request):
    context_dict = {}
    return render(request, 'kinkyCuts/explore.html', context_dict)

def mypictures(request):
    context_dict = {}
    return render(request, 'kinkyCuts/mypictures.html', context_dict)

def myaccount(request):
    context_dict = {}
    return render(request, 'kinkyCuts/myaccount.html', context_dict)

def helpage(request):
    context_dict = {}
    return render(request, 'kinkyCuts/help.html', context_dict)

def sign(request):
    context_dict = {}
    return render(request, 'kinkyCuts/sign.html', context_dict)
