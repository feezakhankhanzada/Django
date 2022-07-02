from pickle import TRUE
from django.db import models

class Tweet(models.Model):

    id = models.CharField(max_length=100 , primary_key=TRUE)
    text = models.CharField(max_length=10000)
    selectedText = models.CharField(max_length=10000)
    sentiments = models.CharField(max_length=1000, default="Some String")

    def __str__(self):
        return self.id