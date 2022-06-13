from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomePlaces.as_view(), name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('contact/', contact, name='contact'),
    path('sales/', sales, name='sales'),
    path('prices/', prices, name='prices'),
    path('add_review/', add_review, name='add_review'),
]
