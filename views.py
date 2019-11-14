from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    dict = {'name': 'This is a dict'}
    return render(request, 'index.html', content=dict)



def about(request):
    return HttpResponse('this is my about page')


def contact(request):
    return HttpResponse('contact us page')