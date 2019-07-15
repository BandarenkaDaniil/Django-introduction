from django.db import models

from users.models import User
from railways.mixins.timestampable import TimestampableModelMixin


class Station(TimestampableModelMixin, models.Model):
    title = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return (
            '{title} ({country})'.format(title=self.title, country=self.country)
        )


class Track(TimestampableModelMixin, models.Model):
    departure_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name='outcoming_tracks'
    )

    arrival_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name='incoming_tracks'
    )
    length = models.PositiveIntegerField()

    def __str__(self):
        return 'Track from {dep_st} to {arr_st}. Length: {length}'.format(
            dep_st=self.departure_station,
            arr_st=self.arrival_station,
            length=self.length
        )


class Route(TimestampableModelMixin, models.Model):
    departure_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="outcoming_routes"
    )

    arrival_station = models.ForeignKey(
        Station,
        on_delete=models.CASCADE,
        related_name="incoming_routes"
    )

    def __str__(self):
        return 'Route from {dep_station} to {arr_station}'.format(
            dep_station=self.departure_station,
            arr_station=self.arrival_station
        )


class RouteItem(TimestampableModelMixin, models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='items'
    )
    track = models.ForeignKey(
        Track,
        on_delete=models.CASCADE,
        related_name='items'
    )
    previous_item = models.ForeignKey(
        'RouteItem',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return 'Route item for {route}, {track}'.format(
            route=self.route,
            track=self.track
        )


class Train(TimestampableModelMixin, models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='trains'
    )

    def __str__(self):
        return 'Train: ID: {id}'.format(id=self.id)


class Ride(TimestampableModelMixin, models.Model):
    route = models.ForeignKey(
        Route,
        on_delete=models.CASCADE,
        related_name='rides'
    )

    cost = models.PositiveIntegerField()

    departure_date = models.DateField()
    departure_time = models.TimeField()

    arrival_date = models.DateField()
    arrival_time = models.TimeField()

    def __str__(self):
        return (
            'Ride. {route}. Departure: {departure} - Arrival {arrival}'.format(
                route=self.route,
                departure=self.departure_date,
                arrival=self.arrival_date
            )
        )


class Ticket(TimestampableModelMixin, models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    ride = models.ForeignKey(
        Ride,
        on_delete=models.CASCADE,
        related_name='tickets'
    )

    def __str__(self):
        return 'Ticket. {customer}. {ride}'.format(
            customer=self.customer,
            ride=self.ride
        )
