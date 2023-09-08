# bagels/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('bagels_game/', views.bagels_game, name='bagels_game'),
]