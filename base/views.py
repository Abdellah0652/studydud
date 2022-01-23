from django.http import HttpResponse
from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'lets larn python '},
    {'id': 2, 'name': 'desing with me '},
    {'id': 3, 'name': 'lets larn python '},
]


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'room.html', context)


def home(request):
    context = {'rooms': rooms}

    return render(request, 'home.html', context)
