from django.shortcuts import render
# for function api view you need it
from rest_framework.decorators import api_view
# for json response it response json format
from rest_framework.response import Response
# all the models
from base.models import City, AMC, Seat, Ticket
# all the model serializer
from .serializer import CitySerializer, AMCSerializer, \
    MovieSerializer, SeatSerializer, TicketSerializer

# function  api view only allow get request
@api_view(["GET"])
def city_api(request):
    # get all the cities from db
    cities = City.objects.all()
    # serializer help us to turn all the db data to json format
    # many= true means there will be more than one entrie
    serializer = CitySerializer(cities, many=True)
    # return json format data like below
    return Response(serializer.data)

# function  api view only allow get request
@api_view(['GET'])
def apiOVerView(request):
    # all the overviews
    apis = {
        "City List": 'cities/',
        "All the theatres in the city": "city/<int:pk>",
        "All the movies in the theatre": "city/<int:ck>/amc/<int:pk>",
        "All the available seats in the movie": "city/<int:ck>/amc/<int:pk>/seat/<str:pk>",

        "Book The seat" : "book_seat/"
    }
    # return json format data like below
    return Response(apis)

# function  api view only allow get request
@api_view(["GET"])
# we get the param for city id
def amc_api(request, pk):
    # get the city match with id
    city = City.objects.get(pk=pk)
    # get all the theatre in the current city
    amcs = city.amc_set.all()
    # serializer help us to turn all the db data to json format
    # many= true means there will be more than one entrie
    serializer = AMCSerializer(amcs, many=True)

    # return json format data like below
    return Response(serializer.data)

# function  api view only allow get request
@api_view(["GET"])
def movie_api(request,ck, pk):
    # get the city match with id
    city = City.objects.get(pk=ck)
    # get the theatre match with id
    amc = city.amc_set.get(pk=pk)
    # amc = AMC.objects.get(pk=pk)
    print(amc)
    # get all the movies in the theatre
    movies = amc.movies.all()
    # serializer help us to turn all the db data to json format
    # many= true means there will be more than one entrie
    serializer = MovieSerializer(movies, many=True)
    # return json format data like below
    return Response(serializer.data)

# function  api view only allow get request
@api_view(["GET"])
def seat_api(request, ck,ak,pk):
    # get the city with the right id
    city = City.objects.get(pk=ck)
    # get the theatre with the right id
    amc = city.amc_set.get(pk=ak)
    # get the movie with the right id
    movie = amc.movies.get(pk=pk)
    # filter all the seats has not been sold
    seats = movie.seat_set.filter(sold=False)
    # seats = Seat.objects.filter(movie__name=pk).filter(sold=False)
    print(seats)
    # serializer help us to turn all the db data to json format
    # many= true means there will be more than one entrie
    serializer = SeatSerializer(seats, many=True)
    # return json format data like below
    return Response(serializer.data)

# function  api view allow both get and post request
@api_view(["GET", "POST"])

def book_api(request):
    if request.method == "GET":
        # get all the tickets in the db
        tickets = Ticket.objects.all()
        # serializer help us to turn all the db data to json format
        # many= true means there will be more than one entrie
        serializer = TicketSerializer(tickets, many=True)
    if request.method == "POST":
        # serializer help us to turn all the db data to json format
        # request.data is json data we get from page
        # it contains right format of db
        # then we put into serializer so we can play with db easily
        serializer = TicketSerializer(data=request.data)
        # if serializer data format is matching with db
        if serializer.is_valid():
            # save the db
            serializer.save()
        print("hello world")
    # return json format data like below
    return Response(serializer.data)

# dummy data you dont need it
@api_view(["POST"])
def test_me(request):
    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    print("hello world")

    return Response(serializer.data)
