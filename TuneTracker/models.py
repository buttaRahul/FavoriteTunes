from django.db import models

# Create your models here.


class Artist(models.Model):


    name = models.TextField(max_length = 40)

    def __str__(self):
        return self.name


class Song(models.Model):

    title = models.TextField(max_length = 50)
    artist = models.ForeignKey(Artist,on_delete = models.CASCADE,related_name = "songs")

    def __str__(self):
        return self.title


