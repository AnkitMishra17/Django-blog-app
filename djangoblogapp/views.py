from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse('This is the Home page.')
    return render(request,'Homepage.html')

def about(request):
    #return HttpResponse('This is the About Page.')
    return render(request,'About.html')
