from django.db import models
from django.utils.translation import ugettext as _

from users.models import User
from railways.mixins.timestampable import TimestampableModelMixin


class Station(TimestampableModelMixin, models.Model):
    title = models.CharField(max_length=40)
    country = models.CharField(max_length=40)

    def __str__(self):
        return 'Station: {title} ({country})'.format(title=self.title,
                                                     country=self.country)


class Track(TimestampableModelMixin, models.Model):
    departure_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                          related_name="tracks_departure")
    arrival_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                        related_name="tracks_arrival")
    length = models.PositiveIntegerField()

    def __str__(self):
        return 'Track. From {dep_st} to {arr_st}. Length: {length}'.format(
            dep_st=self.departure_station,
            arr_st=self.arrival_station,
            length=self.length)


class Route(TimestampableModelMixin, models.Model):
    departure_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                          related_name="routes_departure")
    arrival_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                        related_name="routes_arrival")

    def __str__(self):
        return 'Route. From {dep_station} to {arr_station}'.format(
            dep_station=self.departure_station,
            arr_station=self.arrival_station)


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
        return 'Route item. {route}. Track: {track}'.format(
            route=self.route,
            track=self.track)


class Train(TimestampableModelMixin, models.Model):
    # TRAIN_TYPES = (
    #     ('economy', _('economy')),
    #     ('business', _('business')),
    #     ('comfort', _('comfort'))
    # )
    #
    # type = models.CharField(max_length=10, choices=TRAIN_TYPES)
    route = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self):
        return 'Train: ID: {id}'.format(id=self.id)


class Ride(TimestampableModelMixin, models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()

    def __str__(self):
        return 'Ride. {route}. Departure: {departure} - Arrival {arrival}'.format(
            route=self.route,
            departure=self.departure_date,
            arrival=self.arrival_date)


class Ticket(TimestampableModelMixin, models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)

    def __str__(self):
        return 'Ticket. {customer}. {ride}'.format(
            customer=self.customer,
            ride=self.ride)
