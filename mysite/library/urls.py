from django.urls import path

from . import views

app_name = 'books'
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.books_list, name='books_list'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_info'),
    path('book/create/', views.BookCreateView.as_view(), name='book_create'),
    path('book/<int:pk>/update', views.BookUpdateView.as_view(), name='book_update'),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author_info'),
    path('author/create/', views.AuthorCreateView.as_view(), name='create_author'),
    path('author/<int:pk>/update', views.AuthorUpdateView.as_view(), name='update_author'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name='author_delete'),
]