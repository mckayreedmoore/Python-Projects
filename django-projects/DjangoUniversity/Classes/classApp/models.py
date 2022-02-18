from django.db import models


class djangoClasses(models.Model):
    title = models.CharField(max_length=60)
    courseNum = models.IntegerField()
    instructorName = models.CharField(max_length=60)
    duration = models.FloatField()

    def __str__(self):
        return self.title

    objects = models.Manager()
