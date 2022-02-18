from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60),
    courseNum = models.IntegerField(max_length=10),
    instructorName = models.CharField(max_length=60),
    duration = models.FloatField(max_length=10),

    def __str__(self):
        return self.title
