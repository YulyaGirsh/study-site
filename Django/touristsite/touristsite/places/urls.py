from django.urls import path
from .views import *

urlpatterns = [
    # path('', index, name='home'),
    path('', HomePlaces.as_view(), name='home'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('category/<int:category_id>/', PlacesByCategory.as_view(), name='category'),
    path('places/<int:places_id>/', ViewPlace.as_view(), name='view_place'),
    path('contact/', contact, name='contact'),
    path('sales/', sales, name='sales'),
    path('prices/', prices, name='prices'),
    path('add_review/', add_review, name='add_review'),
    path('test/', test, name='test'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', logoutuser, name='logout'),
]
