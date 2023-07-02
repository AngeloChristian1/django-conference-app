from django.urls import path
from . import views

urlpatterns = [
    path('', views.speaker),
    path('create/', views.create_speaker, name='create_speaker'),
    path('read_one/<id>/', views.read_one_speaker,  name='read_one_speaker'),
    path('read_all/', views.read_all_speaker, name='read_all_speaker'),
    path('delete/<id>/', views.delete_speaker, name='delete_speaker'),
    path('update/<id>/', views.update_speaker, name='update_speaker'),
    path('form/', views.speaker_form, name='speaker_form'),
    path('read_all_delete/', views.delete_speaker_from_all, name='delete_speaker_from_all'),
]