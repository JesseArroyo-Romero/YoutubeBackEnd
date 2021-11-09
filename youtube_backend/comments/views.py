from .models import Comments
from .serializers import CommentsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CommentsList(APIview):

    def get(self, request):
        comments = Comments.objects.all()
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)
