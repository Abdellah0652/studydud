from django.http import HttpResponse
from django.shortcuts import render

from base.models import Room

rooms = [
    {'id': 1, 'name': 'lets larn python '},
    {'id': 2, 'name': 'desing with me '},
    {'id': 3, 'name': 'lets larn python '},
]


def room(request, pk):
    room =Room.objects.get(id=pk)

    context = {'room': room}
    return render(request, 'base/room.html', context)


def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}

    return render(request, 'base/home.html', context)
