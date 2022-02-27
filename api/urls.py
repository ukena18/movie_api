
from django.urls import path, include
from . import views


urlpatterns = [
    # overview
path("",views.apiOVerView, name = "api-overview"),
    # all the cities in the db
path("cities/",views.city_api, name = "city-list"),
    # single city
path("city/<int:pk>",views.amc_api, name = "amc-list"),
    # single city single theatre
path("city/<int:ck>/amc/<int:pk>",views.movie_api, name = "movie-list"),
    # single city single theatre single seat
path("city/<int:ck>/amc/<int:ak>/seat/<str:pk>",views.seat_api, name = "seat-list"),
    # get the ticket
path("book-seat/",views.book_api, name = "book-seat"),
    # dummy test api you don't need it
path("test_me/",views.test_me, name= "test_me" )

]
