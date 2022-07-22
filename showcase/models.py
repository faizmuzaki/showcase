from django.db import models

# Create your models here.
class Author(models.Model):
    npm = models.CharField(max_length=11)
    nama = models.CharField(max_length=64)
    angkatan = models.IntegerField()

    def __str__(self):
       return self.nama

class Project(models.Model):
    judul = models.CharField(max_length=64)
    deskripsi = models.CharField(max_length=1000)
    link_youtube = models.CharField(max_length=64)
    link_cover = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='made_by')

    def __str__(self):
       return self.judul