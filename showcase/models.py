from django.db import models

# Create your models here.
class Author(models.Model):
    npm = models.CharField(max_length=11)
    name = models.CharField(max_length=64)
    gen = models.IntegerField()

class Project(models.Model):
    title = models.CharField(max_length=64)
    desc = models.CharField(max_length=1000)
    link_yt = models.CharField(max_length=64)
    link_cv = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='made_by')