from django.urls import path
from .views import *

urlpatterns = [
    path('list/create/api/', BookListCreateAPI.as_view(), name='booklistcreate'),
    path('delete/update/api/<int:pk>/', BookUpdateDeleteAPI.as_view(), name='booklistcreate'),
    path('book/search/get/', BookSearchGetAPI.as_view(), name='BookSearchGetAPI'),
]