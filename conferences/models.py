import datetime
from datetime import timedelta

# https://djangoproject.com

from django.db import models

#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         verbose_name = 'Category'
#         verbose_name_plural = 'Categories'
#
#     def __str__(self):
#         return self.name
#
#
# #  1 cat -------> Many conf
# #  1 conf ------> 1 cat:
#
#
# class Conference(models.Model):
#     title = models.CharField(max_length=200)
#     date = models.DateTimeField()
#     # category = models.CharField(max_length=100, choices=CONF_CATEGORIES)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.title} - {self.category}"


class Conference(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, default='Unknown')
    organiser = models.CharField(max_length=200, null=False, blank=False, default='Unknown')
    location = models.CharField(max_length=100, null=False, blank=False, default='Unknown')
    date = models.CharField(max_length=100, null=True, blank=True, default='Unknown')
    time = models.CharField(max_length=100, null=True, blank=True, default='Unknown')
    about = models.TextField()

    def __str__(self):
        return self.title