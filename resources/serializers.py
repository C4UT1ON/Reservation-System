from .models import *
from rest_framework import serializers


class ItemSerializer (serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'title', 'description', 'location', 'bookings')


class LocationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'title', 'description', 'bookings')


class BookingSerializer (serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('title', 'start', 'end', 'client')


class ClientSerializer (serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('first_name', 'last_name')
