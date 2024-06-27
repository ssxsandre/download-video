from django.db import models

class Video(models.Model):
    url = models.URLField(max_length=200)
    title = models.CharField(max_length=200)