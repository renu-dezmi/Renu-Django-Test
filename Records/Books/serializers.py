from rest_framework import serializers
from .models import Drive

# class BookSerializer(serializers.ModelSerializer):
# class Meta():
# model = Books
# fields = ('bookId', 'bookName')
#
# class AuthorSerializer(serializers.ModelSerializer):
# class Meta():
#     model = Authors
#     fields = ('authorName', 'authorEmail')


class AuthorAndBook(serializers.ModelSerializer):
    class Meta():
        model = Drive
        fields = ('authorName', 'authorEmail', 'bookId', 'bookName')
