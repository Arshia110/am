from django.shortcuts import render
from django.http import HttpResponse

def index_view(requests):
    return HttpResponse('1 arshia home')
def about_view(requests):
    return HttpResponse('about arshia')
def contact_view(requests):
    return HttpResponse('2 arshia contact')



    
