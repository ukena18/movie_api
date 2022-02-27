from django.contrib import admin
# Get all the db models
from .models import Customer, City, AMC, Movie, Ticket, Seat



admin.site.register(Customer)
admin.site.register(City)
admin.site.register(AMC)
admin.site.register(Movie)
admin.site.register(Ticket)
admin.site.register(Seat)
