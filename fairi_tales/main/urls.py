
from django.urls import path
from . import views





urlpatterns = [
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('story_list', views.story_list, name='story_list'),
    path('search_stories', views.search_stories, name='search_stories'),
    path('story_list/<int:pk>/', views.story_detail, name='story_detail'),

]
