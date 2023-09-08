# bagels/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='about_game'),
    path('bagels_game/', views.bagels_game, name='bagels_game'),
]