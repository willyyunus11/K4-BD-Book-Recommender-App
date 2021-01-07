from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('first-5-books/', views.firstRating),

]
