from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('author', views.author, name='blog-author'),
    path('story_1', views.TheStoriesOfOEC_1, name="blog-TheStoriesOfOEC_1"),
    path('story_2', views.TheStoriesOfOEC_2, name="blog-TheStoriesOfOEC_2"),
]
