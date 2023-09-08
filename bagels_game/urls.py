# bagels/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about_bagels_game'),
    path('start/', views.bagels_game, name='bagels_game'),
]