from django.db import models

class Post(models.Model):
    publish_date = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=255)
    content = models.TextField()


class Author(models.Model):
    usermame = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
