from django.urls import path
from . import views

urlpatterns = [
    path('', views.conference, name='speaker'),
    path('create/', views.create_conference,  name='create_speaker'),
    path('read_one/<id>/', views.read_one_conference, name='read_one_speaker'),
    path('read_all/', views.read_all_conference, name='read_all_speaker'),
    path('delete/<id>/', views.delete_conference, name='delete_speaker'),
    path('update/<id>/', views.update_conference, name='update_speaker'),
]