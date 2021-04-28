from djnago.urls import path
from .import views


urlpatterns = [
    path('', views.apioverview, name='apioverview'),
    path('/Song-list', views.showall, name='Song-list'),
    path('/Song-detail', views.showall, name='Song-detail'),
    path('/Song-Create', views.showall, name='Song-Create'),
    path('/Song-Update', views.showall, name='Song-Update'),
    path('/Song-Delete', views.showall, name='Song-Delete'),
    path('/Podacst-list', views.showall, name='Podcast-list'),
    path('/Podacst-detail', views.showall, name='Podcast-detail'),
    path('/Podacst-Create', views.showall, name='Podcast-Create'),
    path('/Podacst-Update', views.showall, name='Podcast-Update'),
    path('/Podacst-Delete', views.showall, name='Podcast-Delete'),
    path('/Audiobook-list', views.showall, name='Audiobook-list'),
    path('/Audiobook-detail', views.showall, name='Audiobook-detail'),
    path('/Audiobook-Create', views.showall, name='Audiobook-Create'),
    path('/Audiobook-Update', views.showall, name='Audiobook-Update'),
    path('/Audiobook-Delete', views.showall, name='Audiobook-Delete'),
]
