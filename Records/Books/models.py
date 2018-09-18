from datetime import datetime

from django.db import models


class CustomModel(models.Model):
    createdAt = models.DateTimeField(default=datetime.utcnow())
    modifiedAt = models.DateTimeField(default=datetime.utcnow())

    class Meta:
        abstract = True


class Books(models.Model):
    bookId = models.CharField(max_length=30, unique=True)
    bookName = models.CharField(max_length=40)

    class Meta:
        abstract = True


class Authors(CustomModel):
    authorName = models.CharField(max_length=60)
    authorEmail = models.EmailField(max_length=100)


class Drive(Authors, Books):
    pass


