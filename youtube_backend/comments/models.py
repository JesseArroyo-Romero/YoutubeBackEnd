from django.db import models

# Create your models here.


class Comments(models.Model):
    video_id = models.CharField(max_length=50)
    comment = models.CharField(max_length=200)
    like = models.IntegerField(blank=True, null=True)
    dislike = models.IntegerField(blank=True, null=True)
