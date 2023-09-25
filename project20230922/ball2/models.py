from django.db import models

class Report(models.Model):
    user = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    count = models.IntegerField(max_length=200)
