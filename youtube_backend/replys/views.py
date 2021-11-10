from .models import Replys
from .serializers import ReplysSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ReplysList(APIView):

    def get(self, request):
        replys = Replys.objects.all()
        serializer = ReplysSerializer(replys, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplysSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReplysDetail(APIView):

    def get_object(self, pk):
        try:
            return Replys.objects.get(pk=pk)
        except Replys.DoesNotExist:
            raise Http404

    # get by id
    def get(self, request, pk):
        replys = self.get_object(pk)
        serializer = ReplysSerializer(replys)
        return Response(serializer.data)

    # update
    def put(self, request, pk):
        replys = self.get_object(pk)
        serializer = ReplysSerializer(replys, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete
    def delete(self, request, pk):
        replys = self.get_object(pk)
        replys.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
