from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import AuthorSerializer, QuoteSerializer
from ..models import Author, Quote


class AuthorList(APIView):
    """
    List all quotes, or create new

    """
    def get(self, request, format=None):
        task_lists = Author.objects.all()
        serializer = AuthorSerializer(task_lists, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetail(APIView):
    """
    Retrieve, update or delete a task list instance
    """
    def get(self, request, pk, format=None):
        task_list = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(task_list)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task_list = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(task_list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task_list = get_object_or_404(Author, pk=pk)
        task_list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class QuoteList(APIView):
    """
    List all quotes or create new
    """
    def get(self, request, format=None):
        tasks = Quote.objects.all()
        serializer = QuoteSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuoteDetail(APIView):
    """
    Retrieve, update or delete a quote instance
    """
    def get(self, request, pk, format=None):
        task = get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task = get_object_or_404(Quote, pk=pk)
        serializer = QuoteSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = get_object_or_404(Quote, pk=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


###############
### Generic CBV
###############
# from rest_framework import generics, permissions
# class AuthorListAPIView(generics.ListAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#     permission_classes = [permissions.IsAuthenticated]
#
#
# class QuoteListAPIView(generics.ListAPIView):
#     queryset = Quote.objects.all()
#     serializer_class = QuoteSerializer
#     permission_classes = [permissions.IsAuthenticated]
