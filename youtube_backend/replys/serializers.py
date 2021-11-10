from rest_framework import serializers
from .models import Replys


class ReplysSerializer (serializers.ModelSerializer):
    class Meta:
        model = Replys
        fields = ['comment', 'comment_id']
