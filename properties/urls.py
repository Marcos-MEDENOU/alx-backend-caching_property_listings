from django.urls import path
from . import views

urlpatterns = [
    # We'll add property endpoints here later
    path('properties/', views.property_list, name='property-list'),
]
