from django.db import models
from django.urls import reverse
from django import forms

class Album(models.Model):
    artist=models.CharField(max_length=250)
    album_title=models.CharField(max_length=250)
    genre=models.CharField(max_length=250)
    album_logo=models.CharField(max_length=10000)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})


    def __str__(self):
        return self.album_title+'-'+self.artist

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type=models.CharField(max_length=250)
    song_title=models.CharField(max_length=250)

    def __buffer__(self):
        return self.song_title   

class Artist(models.Model):
    name=models.CharField(max_length=100)
    album=models.CharField(max_length=100)

class ArtistForm(forms.ModelForm):
    class Meta:
       model=Artist
       fields=['name','album']