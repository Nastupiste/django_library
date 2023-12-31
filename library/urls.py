from django.urls import path
from .views import *

urlpatterns = [
    path('', ListBookView.as_view(), name='book_list'),
    path('book/add', BookAdd.as_view(), name='add_book'),
    path('book/details/<int:pk>', BookDetailsView.as_view(), name='book_details'),
    path('book/edit/<int:pk>', BookEdit.as_view(), name='book_edit'),
]
