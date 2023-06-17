from django.urls import path
from .views import *

urlpatterns = [
    path('list/create/api/', BookListCreateAPI.as_view(), name='booklistcreate'),  # list and create API
    path('delete/update/api/<int:pk>/', BookUpdateDeleteAPI.as_view(), name='booklistcreate'),  # update and delete API
    path('book/search/get/', BookSearchGetAPI.as_view(), name='BookSearchGetAPI'),  # Book filter API
]
