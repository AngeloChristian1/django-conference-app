from django.db import models

# Create your models here.
class Speaker(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    organisation = models.CharField(max_length=200, null=False, blank=False)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    topic = models.TextField()
    biography = models.TextField()


    def __str__(self):
        return self.name


