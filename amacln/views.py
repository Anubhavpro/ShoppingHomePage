from django.shortcuts import render
from django.views import View
# Create your views here.

def amazclone(request):
    return render(request,'amacln/index.html')

