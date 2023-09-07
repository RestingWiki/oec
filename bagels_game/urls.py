# bagels/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.bagels_game, name='bagels_game'),
]
