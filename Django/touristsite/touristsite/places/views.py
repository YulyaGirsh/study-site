from django.shortcuts import render
from django.http import HttpResponse
from .models import Places


def index(request):
    places = Places.objects.all()
    return HttpResponse('Hello')
    # return render(request, 'places.index', {'places':places, 'title': 'Список направлений'})
