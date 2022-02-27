# import serializer to ctreate model serializer
from rest_framework import serializers
# get all the models from base app
from base.models import City, AMC, Movie, Seat, Ticket


# Those all serializer for api sending and get api to transform to
# django data easily

# serialize City model
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

# serialize AMC model
class AMCSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMC
        fields = "__all__"

# serialize Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

# serialize Seat model
class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = "__all__"

# serialize Ticket model
class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"
