from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import City, AMC, Seat, Ticket
from .serializer import CitySerializer, AMCSerializer, MovieSerializer, SeatSerializer, TicketSerializer

@api_view(["GET"])
def city_api(request):
    cities = City.objects.all()
    serializer= CitySerializer(cities, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def apiOVerView(request):
    apis = {
        "cities/": "city-list",
        "city/<int:pk>": "amc-list",
        "amc/<int:pk>": "movie-list",
        "seat/<str:pk>": "seat-list"
         }
    return Response(apis)


@api_view(["GET"])
def amc_api(request,pk):
    city = City.objects.get(pk=pk)
    amcs = city.amc_set.all()
    serializer = AMCSerializer(amcs,many=True)

    return Response(serializer.data)



@api_view(["GET"])
def movie_api(request,pk):
    amc = AMC.objects.get(pk=pk)
    print(amc)
    movies = amc.movies.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)



@api_view(["GET"])
def seat_api(request,pk):
    seats = Seat.objects.filter(movie__name = pk).filter(sold = False)
    print(seats)
    serializer = SeatSerializer(seats, many=True)
    return Response(serializer.data)

@api_view(["GET","POST"])
def book_api(request):

    if request.method == "GET":
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
    if request.method == "POST":
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        print("hello world")

    return Response(serializer.data)




@api_view(["POST"])
def test_me(request):

    serializer = CitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    print("hello world")

    return Response(serializer.data)


