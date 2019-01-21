import itertools

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from rest_framework.exceptions import ValidationError


from railways.models import (
    Ride,
    Route,
    RouteItem,
    Station,
    Ticket,
    Track,
    Train,
)

from railways.utils import calculate_amount

from railways.utils import calculate_amount


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ('id', 'route',)


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'title', 'country')
        validators = [
            UniqueTogetherValidator(
                queryset=Station.objects.all(),
                fields=('title', 'country'),
                message='This station already exists'
            )
        ]


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'departure_station', 'arrival_station', 'length')

    def validate(self, attrs):
        if attrs['departure_station'] == attrs['arrival_station']:
            raise ValidationError('Track cannot connect same stations')


class RouteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteItem
        fields = ('track', )


class RouteSerializer(serializers.ModelSerializer):
    """TODO: add update method"""

    items = RouteItemSerializer(many=True)
    trains = TrainSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'trains', 'items', )

    @staticmethod
    def validate_items(attrs):
        """
            Checks if got items form correct sequence of tracks.
        """
        if not attrs:
            raise ValidationError("No items input")

        tracks = list(i['track'] for i in attrs)

        if len(tracks) > 1:
            # form two independent iterators to get
            # tracks pairs like (1,2), (2,3), (3, 4) and so on
            iter1, iter2 = itertools.tee(tracks)
            next(iter2)

            tracks_pairs = list(zip(iter1, iter2))

            for pair in tracks_pairs:
                # check every pair to make sure that arrival station
                # of one track is equal to another's departure
                if pair[0].arrival_station != pair[1].departure_station:
                    raise ValidationError(
                        'Given tracks don\'t form correct sequence'
                    )

        return attrs

    def create(self, validated_data):
        new_track_list = [item['track'] for item in validated_data['items']]

        # Route departure and arrival stations are
        # departure station of the first track in sequence and
        # arrival of the last.
        # Even if sequence consists of one track.
        route = Route.objects.create(
            departure_station=new_track_list[0].departure_station,
            arrival_station=new_track_list[-1].arrival_station
        )

        # previous item of the first route item
        # is always null
        previous_item = None
        for track in new_track_list:
            item = RouteItem.objects.create(
                route=route,
                track=track,
                previous_item=previous_item
            )
            previous_item = item

        return route

    def update(self, instance, validated_data):
        new_track_list = [item['track'] for item in validated_data['items']]

        # Route departure and arrival stations are
        # departure station of the first track in sequence and
        # arrival of the last.
        # Even if sequence consists of one track.
        Route.objects.filter(id=instance.id).update(
            departure_station=new_track_list[0].departure_station,
            arrival_station=new_track_list[-1].arrival_station)

        # delete all items and create new
        # imho it's easier to understanding
        # than, for example, invent smart algorithms :)
        RouteItem.objects.filter(route=instance).delete()

        # previous item of the first route item
        # is always null
        previous_item = None
        for track in new_track_list:
            item = RouteItem.objects.create(
                route=instance,
                track=track,
                previous_item=previous_item
            )
            previous_item = item

        return instance


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'customer', 'ride')


class UserTicketsSerializer(serializers.ModelSerializer):
    departure_station = serializers.ReadOnlyField(source='ride.route.departure_station.title')
    arrival_station = serializers.ReadOnlyField(source='ride.route.arrival_station.title')
    departure_date = serializers.ReadOnlyField(source='ride.departure_date')
    arrival_date = serializers.ReadOnlyField(source='ride.arrival_date')

    class Meta:
        model = Ticket
        fields = ('departure_station', 'arrival_station',
                  'departure_date', 'arrival_date')


class TicketBuySerializer(serializers.Serializer):
    departure_station = serializers.CharField()
    arrival_station = serializers.CharField()
    departure_date = serializers.DateField()
    departure_time = serializers.TimeField()

    def create(self, validated_data):
        departure_station = Station.objects.get(title=validated_data['departure_station'])
        arrival_station = Station.objects.get(title=validated_data['arrival_station'])

        ride = Ride.objects.get(route__departure_station=departure_station,
                                route__arrival_station=arrival_station,
                                departure_date=validated_data['departure_date'],
                                departure_time=validated_data['departure_time'])

        customer = self.context['user']

        return Ticket.objects.create(customer=customer, ride=ride)


class RideSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
    departure_station = serializers.ReadOnlyField(source='route.departure_station.title')
    arrival_station = serializers.ReadOnlyField(source='route.arrival_station.title')

    class Meta:
        model = Ride
        fields = ('id', 'route', 'amount',
                  'departure_station', 'arrival_station',
                  'departure_date', 'arrival_date',
                  'departure_time', 'arrival_time',
                  'tickets')
        read_only_fields = ('amount', )

    def validate(self, attrs):
        if attrs['arrival_date'] <= attrs['departure_date']:
            raise ValidationError('Arrival cannot be after Departure')

        return attrs

    def create(self, validated_data):
        validated_data['amount'] = calculate_amount(validated_data['route'])

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # if this ride's route is being changed
        # we need to recalculate its amount
        if instance.route != validated_data['route']:
            validated_data['amount'] = calculate_amount(validated_data['route'])

        return super().update(instance, validated_data)


class SpecificRideSerializer(serializers.ModelSerializer):
    departure_station = serializers.ReadOnlyField(source='route.departure_station.title')
    arrival_station = serializers.ReadOnlyField(source='route.arrival_station.title')

    class Meta:
        model = Ride
        fields = ('amount',
                  'departure_station', 'arrival_station',
                  'departure_date',    'arrival_date',
                  'departure_time',    'arrival_time')
