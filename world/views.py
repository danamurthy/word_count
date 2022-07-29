from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse('NOW I AM IN ASSOCTION CLASS')
def word(request):
    dictonary={'name':'danamurthy'}
    return render(request,'index.html')
def count(request):
    return render(request,'count.html')