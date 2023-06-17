import django_filters
from django.shortcuts import render
from django_filters import NumberFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import BookSerializer
from .models import Book
from django_filters.rest_framework import DjangoFilterBackend


# create View
# show the list of book and create new book details
class BookListCreateAPI(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# update and delete the books by id
class BookUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# This is filter to manage the books or search the book according to the fields
class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(lookup_expr="icontains")
    publication_year = django_filters.DateFilter(field_name='publication_year', lookup_expr='exact')
    publication_year_start = django_filters.DateFilter(field_name='publication_year', lookup_expr='gte')
    publication_year_end = django_filters.DateFilter(field_name='publication_year', lookup_expr='lte')

    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'publication_year_start', 'publication_year_end']


# manage the filter method
class BookSearchGetAPI(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


