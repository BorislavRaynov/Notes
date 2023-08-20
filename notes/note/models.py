from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=30)
    image = models.URLField()
    content = models.TextField()
