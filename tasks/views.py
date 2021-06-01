from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def helloword(request):
    return HttpResponse('hello word')

def tasklist(request):
    return render(request, 'tasks/list.html')
