# Define the models for the music platform:
from django.db import models
from django.contrib.auth.models import User

class TonePreset(models.Model):
    name = models.CharField(max_length=100)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to='tone_presets/')

class Comment(models.Model):
    preset = models.ForeignKey(TonePreset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    preset = models.ForeignKey(TonePreset, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
