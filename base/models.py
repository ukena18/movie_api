from django.db import models
# get the user models
from django.contrib.auth.models import User
# get the max and min value for integer field
from django.core.validators import MaxValueValidator, MinValueValidator
# those are for signals before saving and after saving
from django.db.models.signals import pre_save,post_save

# Customer model so Customer can buy ticket
class Customer(models.Model):
    # get the user model as one to one field
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


# City class
class City(models.Model):
    # # it contains only name
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Movie(models.Model):
    # movie will have name and ticket can be sell
    name = models.CharField(max_length=200)
    # customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    tickets = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class AMC(models.Model):
    # theatre has city name and whick movies can play the theatre
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

# each theatre movie will have 50 seat model
# that is around 1000 seat in the db
class Seat(models.Model):
    # each seat belong to specific theatre's movie
    # and it will have the seat no independent of id
    # and also if it is sold or not I change it in the signal
    amc = models.ForeignKey(AMC,on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    seat_no = models.IntegerField(validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ])
    # that will be change in the signals
    sold = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return f"seat no :{str(self.seat_no)}----id :{self.id} ---{self.movie.name}"

# You have ticket wwhen you buy the seat in the movie
class Ticket(models.Model):
    # seat_no  = models.AutoField(primary_key=True)
    # each ticket will have seat no cutomer and movie
    seat_no = models.OneToOneField(Seat,on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return f"ticket_id: {self.id}----seat id :{self.seat_no.id} ---{self.movie.name}"




