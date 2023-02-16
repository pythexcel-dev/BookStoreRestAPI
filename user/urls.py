from django.urls import path
from .views import (RegisterAPIView,
LoginAPIView,
MyUserDataAPIView,
MyUserProfileAPIView,
AuthorDetailsAPIView,
DeleteAuthorAPIView,
BookCreateAPIView,
BooksAPIView,
BookGetUpdateAPIView,
AuthorBookDeleteAPIView,
AdminBookDeleteAPIView,
LogoutAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),   
    path('login/', LoginAPIView.as_view()),         
    path('data/', MyUserDataAPIView.as_view()),
    path('profile/', MyUserProfileAPIView.as_view()),
    path('authors/', AuthorDetailsAPIView.as_view()),             
    path('deleteauthor/<int:pk>/', DeleteAuthorAPIView.as_view()),   
    path('createbook/', BookCreateAPIView.as_view()),        
    path('books/', BooksAPIView.as_view()),
    path('book/<int:pk>/', BookGetUpdateAPIView.as_view()),
    path('authorbook/<int:pk>/', AuthorBookDeleteAPIView.as_view()),
    path('adminbook/<int:pk>/', AdminBookDeleteAPIView.as_view()),   
    path('logout/', LogoutAPIView.as_view()),
]