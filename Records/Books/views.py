import json

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser, FormParser
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from .models import Drive
from .serializers import AuthorAndBook


class AuthorAndBookView(APIView):
    parser_classes = (JSONParser, FormParser)

    def post(self, request, *args, **kwargs):
        author_serializer = AuthorAndBook(data=request.data)
        if author_serializer.is_valid():
            author_serializer.save()
            return Response(author_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(author_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        authors = Drive.objects.all()
        response_to_send = json.loads(serializers.serialize('json', authors))
        return Response(response_to_send, status.HTTP_200_OK)

    def put(self, request):
        data = request.data
        bookId = data['bookId']
        name = data['bookName']
        book = Drive.objects.get(bookId=bookId)
        book.bookName = name
        book.save()
        return Response(json.loads(serializers.serialize('json', [book])), status.HTTP_205_RESET_CONTENT)

    def delete(self, request):
        bookId = request.data['bookId']
        book = Drive.objects.get(bookId=bookId)
        book.delete()
        return Response({}, status.HTTP_200_OK)


