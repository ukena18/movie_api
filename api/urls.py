
from django.urls import path, include
from . import views


urlpatterns = [
path("",views.apiOVerView, name = "api-overview"),
path("cities/",views.city_api, name = "city-list"),
path("city/<int:pk>",views.amc_api, name = "amc-list"),
path("city/<int:ck>/amc/<int:pk>",views.movie_api, name = "movie-list"),
path("city/<int:ck>/amc/<int:ak>/seat/<str:pk>",views.seat_api, name = "seat-list"),
path("book-seat/",views.book_api, name = "book-seat"),

path("test_me/",views.test_me, name= "test_me" )

]
