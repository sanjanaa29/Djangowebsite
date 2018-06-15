from django.db import models
from django import forms

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    album_logo=models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title+'--'+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=250)
    song_title=models.CharField(max_length=250)

class Artist(models.Model):
    name=models.CharField(max_length=100)
    album=models.CharField(max_length=100)

class ArtistForm(forms.ModelForm):
    class Meta:
       model=Artist
       fields=['name','album']