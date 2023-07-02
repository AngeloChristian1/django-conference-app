from django.shortcuts import render
from django.forms import ModelForm
from .models import Speaker


class speakerForm(ModelForm):
    class Meta:
        model = Speaker
        fields = '__all__'


