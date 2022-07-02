from .models import *
from django.shortcuts import render
from django.http import HttpResponse 

def main(request):
    title = 'Main Page'
    myapp_tweet = Tweet.objects.all()
    context = {'title': title,
               'myapp_tweet': myapp_tweet}
    return render(request, 'myapp/main.html', context)


def register(request):
	return render(request, 'register.html')
	
def blank(request):
	return HttpResponse('Welcome to plus2net')

