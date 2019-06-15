from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return self.first_name + '' + self.last_name


class Booking(models.Model):
    title = models.CharField(max_length=100)
    start = models.DateTimeField()
    end = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Location (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="A location type Item")
    bookings = models.ManyToManyField(Booking, related_name='locations', null=True)

    def __str__(self):
        return self.title


class Item (models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="A regular business item")
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=True)
    bookings = models.ManyToManyField(Booking, related_name='items', null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['location']
