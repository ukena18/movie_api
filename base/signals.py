# after db receiving model instance
from django.db.models.signals import post_save
# the model receiver
from django.dispatch import receiver

from .models import City, AMC, Seat, Ticket

# receiver for signal after save as model instance
# and model will be ticket
@receiver(post_save, sender=Ticket)
# instance is data
# created is if it is created but not updated
# kwargs is for anything else
def create_ticket(sender,instance,created, **kwargs):
    # if it is not updated but created
    if created:
        # check the istance seat_no id and
        # find the seat we are looking for it
        seat = Seat.objects.get(pk = instance.seat_no.id)
        # change sold to true
        seat.sold = True
        # save the seat so it will not show in the avaiable seats
        seat.save()
        print(seat)
        # if the movie name is and the movie which seat belongs match
        # then save the instance to db
        if instance.seat_no.movie.name == instance.movie.name:
            instance.save()
            print("hello World")
        else:
            raise ValueError
    

