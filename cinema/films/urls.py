from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeFilms.as_view(), name='home'),
    path('films/<int:films_id>', ViewFilms.as_view(), name='view_films'),
    path('films/add_films/', CreateFilms.as_view(), name='add_films'),
    path('price/', price, name='price'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),


]

