from django.shortcuts import render
from django.http import HttpResponse
from .models import Places


def index(request):
    places = Places.objects.all()
    return render(request, 'places/index.html', {'places': places, 'title': 'Список направлений'})
