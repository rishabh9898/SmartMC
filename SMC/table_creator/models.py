from django.db import models

# Create your models here.
from embed_video.fields import EmbedVideoField

class Item(models.Model):
    video = EmbedVideoField()