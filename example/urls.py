from django.urls import path, include
# from .views import HelloAPI, bookAPI, booksAPI
from .views import BookAPI, BooksAPI

urlpatterns = [
    # path('hello/', HelloAPI),

    # fbv url 연결
    # path('fbv/books/', booksAPI),
    # path('fbv/book/<int:bid>/', bookAPI),

    # cbv url 연결    
    path('cbv/books', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),
]