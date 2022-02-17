from django.db import models


# Create your models here.

PREFIX_CHOICES = {

    ('Mr.','Mr.'),
    ('Ms.','Ms.'),
    ('Mrs.','Mrs.'),
}

class profile(models.Model):
    prefix = models.CharField(max_length=10, default="none", choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=120)
    username = models.CharField(max_length=120)

    objects = models.Manager()

    def __str__(self):
        return self.first_name
