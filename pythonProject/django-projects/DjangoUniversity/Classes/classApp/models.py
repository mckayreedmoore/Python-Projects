from django.db import models

# Create your models here.
class djangoClasses (models.Model):
    title = models.CharField(max_length=60),
    courseNumber = models.IntegerField(max_length=8),
    instructorName = models.CharField(max_length=60),
    duration = models.FloatField(max_length=10),
