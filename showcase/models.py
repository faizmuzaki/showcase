from django.db import models
from .url_handler import video_id

# Create your models here.
class Author(models.Model):
    npm = models.CharField(max_length=11)
    nama = models.CharField(max_length=64)
    program_studi = models.CharField(max_length=64, default='Ilmu Komputer/Manajemen Informatika')
    angkatan = models.IntegerField()

    def __str__(self):
       return self.nama

class Project(models.Model):
    judul = models.CharField(max_length=64)
    deskripsi = models.TextField(max_length=1000)
    link_youtube = models.CharField(max_length=64)
    link_cover = models.CharField(max_length=500)
    link_github = models.CharField(max_length=500, default='')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='made_by')

    # This should touch before saving
    def save(self, *args, **kwargs):
        self.link_youtube = "https://www.youtube.com/embed/" + video_id(self.link_youtube)
        super(Project, self).save(*args, **kwargs)

    def __str__(self):
       return self.judul
