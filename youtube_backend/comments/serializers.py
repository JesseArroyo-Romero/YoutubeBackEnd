from _typeshed import SupportsNoArgReadline
from rest_framework import serializers
from .models import Comments


class CommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'video_id', 'comment', 'like', 'dislike']
