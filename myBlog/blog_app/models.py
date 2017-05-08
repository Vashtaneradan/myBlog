from django.db import models
import datetime
from datetime import date


class Post(models.Model):
    publish_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return str(self.publish_date.strftime("%d/%m/%Y") + ' ' + str(self.title))  # Datum formatiert ausgeben mit title


class Author(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username.upper()  # gibt String aus username zurück
