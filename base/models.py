from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import pre_save,post_save


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


### All Done
class City(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    # customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    tickets = models.IntegerField(default=100)

    def __str__(self):
        return self.name

### ALL DONE
class AMC(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    movies = models.ManyToManyField(Movie)

    def __str__(self):
        return self.name

class Seat(models.Model):
    amc = models.ForeignKey(AMC,on_delete=models.SET_NULL, blank=True, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_no = models.IntegerField(validators=[
            MaxValueValidator(50),
            MinValueValidator(1)
        ])
    sold = models.BooleanField(default=False,null=True,blank=True)

    def __str__(self):
        return f"seat no :{str(self.seat_no)}----id :{self.id} ---{self.movie.name}"

class Ticket(models.Model):
    # seat_no  = models.AutoField(primary_key=True)
    seat_no = models.OneToOneField(Seat,on_delete=models.CASCADE, null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return f"ticket_id: {self.id}----seat id :{self.seat_no.id} ---{self.movie.name}"




