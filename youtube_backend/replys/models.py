from django.db import models

# Create your models here.


class Replys(models.Model):
    comment = models.ForeignKey(
        'comments.Comments', blank=True, null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
