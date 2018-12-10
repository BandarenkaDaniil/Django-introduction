from django.db import models
from django.utils.translation import ugettext as _

from users.models import User
from railways.mixins.timestampable import TimestampableModelMixin


class Train(TimestampableModelMixin, models.Model):
    TRAIN_TYPES = (
        ('business', _('business')),
        ('economy', _('economy')),
        ('freight', _('freight'))
    )
    type = models.CharField(max_length=10, choices=TRAIN_TYPES)

    def __str__(self):
        return 'Train: ID: {id} Type: {type}'.format(id=self.id, type=self.type)


class Station(TimestampableModelMixin, models.Model):
    title = models.CharField(max_length=40)
    country = models.CharField(max_length=40, null=True)
    longitude = models.DecimalField(max_digits=4, decimal_places=2)
    latitude = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return 'Station: {title} ({country})'.format(title=self.title,
                                                     country=self.country)


class Ride(TimestampableModelMixin, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    departure_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                          related_name="where_from")
    arrival_station = models.ForeignKey(Station, on_delete=models.CASCADE,
                                        related_name="where_to")

    def __str__(self):
        return 'Ride of {user} user, train ID: {trainID}, from {dep_station} ' \
               'to {arr_station}'.format(user=self.user, trainID=self.train.id,
                                         dep_station=self.departure_station,
                                         arr_station=self.arrival_station)
