from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import ListView
from .models import Places, Categories, Sales, Review
from .forms import ReviewForm2


class HomePlaces(ListView):
    model = Places
    template_name = 'places/index.html'
    context_object_name = 'places'
    extra_context = {'title': 'Главная'}


def index(request):
    places = Places.objects.all()
    categories = Categories.objects.all()
    return render(request, 'places/index.html',
                  {'places': places, 'title': 'Список направлений', 'category': categories})


def get_category(request, category_id):
    places = Places.objects.filter(category_id=category_id)
    categories = Categories.objects.all()
    category = Categories.objects.get(pk=category_id)
    return render(request, 'places/category.html', {'places': places, 'category': category, 'categories': categories})


def contact(request):
    return render(request, 'places/contact.html')


def sales(request):
    sales = Sales.objects.all()
    return render(request, 'places/sales.html', {'sales': sales})


def prices(request):
    places = Places.objects.all()
    return render(request, 'places/prices.html', {'places': places})


def add_review(request):
    if request.method == 'POST':
        form = ReviewForm2(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            Review.objects.create(**form.cleaned_data)
            # reviews = form.save()
            return redirect('home')

    else:
        form = ReviewForm2()
    return render(request, 'places/add_review.html', {'form': form})
