from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import City, AMC, Seat, Ticket
from .models import Seat

@receiver(post_save, sender=Ticket)
def create_ticket(sender,instance,created, **kwargs):



    if created:
        seat = Seat.objects.get(pk = instance.seat_no.id)
        seat.sold = True
        seat.save()
        print(seat)
        if instance.seat_no.movie.name == instance.movie.name:
            instance.save()
            print("hello World")
        else:
            raise ValueError
    

