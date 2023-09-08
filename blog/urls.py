from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about', views.about, name='blog-about'),
    path('story_1', views.TheStoriesOfOEC_1, name="blog-TheStoriesOfOEC_1"),
    path('story_2', views.TheStoriesOfOEC_2, name="blog-TheStoriesOfOEC_2"),
    # path('hello', views.hello, name='blog-hello'),
]
