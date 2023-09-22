from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI
from .views import BookAPI, BooksAPI
from .views import BookAPIMixins, BooksAPIMixins
from .views import BookAPIGenerics, BooksAPIGenerics


urlpatterns = [
    path('hello/', HelloAPI),

    # fbv url 연결
    path('fbv/books/', booksAPI),
    path('fbv/book/<int:bid>/', bookAPI),

    # cbv url 연결    
    path('cbv/books', BooksAPI.as_view()),
    path('cbv/book/<int:bid>/', BookAPI.as_view()),

    # cbv by mixins url 연결
    path('mixin/books/', BooksAPIMixins.as_view()),
    path('mixin/book/<int:bid>/', BookAPIMixins.as_view()),

    # cbv by generics url 연결
    path('generics/books/', BooksAPIGenerics.as_view()),
    path('generics/book/<int:bid>/', BookAPIGenerics.as_view()),
    

]