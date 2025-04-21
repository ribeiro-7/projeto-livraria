from rest_framework import viewsets
from books.api import serializers
from books import models
from rest_framework.permissions import IsAuthenticated

class BooksViewset(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )

    serializer_class = serializers.BooksSerializer
    queryset  = models.Books.objects.all()