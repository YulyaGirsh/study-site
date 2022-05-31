from django.shortcuts import render
from django.http import HttpResponse
from .models import Places, Categories, Sales
from django.template import loader


def index(request):
    places = Places.objects.all()
    categories = Categories.objects.all()
    return render(request, 'places/index.html', {'places': places, 'title': 'Список направлений', 'category' : categories})


def get_category(request, category_id):
    places = Places.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    category = Categories.objects.get(pk=category_id)
    return render(request,  'places/category.html', {'places': places, 'category': category, 'categories': categories})


def contact(request):
    return render(request, 'places/contact.html')


def sales(request):
    sales = Sales.objects.all()
    return render(request, 'places/sales.html', {'sales': sales})
