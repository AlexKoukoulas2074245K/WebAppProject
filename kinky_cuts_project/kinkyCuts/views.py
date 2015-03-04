from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {};
    return render(request, 'kinkyCuts/index.html', context_dict);
