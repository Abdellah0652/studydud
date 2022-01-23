from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('home')

def room(request):
    return render(request,'room.html')
