from django import template
from django.db.models import Count, F
from mainpage.models import Categories

register = template.Library()


@register.simple_tag
def get_categories():
    return Categories.objects.all()


@register.inclusion_tag('mainpage/list_categories.html')
def show_categories(arg1='Hello', arg2='world'):
    categories = Categories.objects.annotate(cnt=Count('places', filter=F('places__is_published'))).filter(cnt__gt=0)
    return {'categories': categories}
