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

from users.models import User

from railways.utils import calculate_route_cost


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
    departure_station = serializers.CharField(
        source='track.departure_station.title'
    )
    arrival_station = serializers.CharField(
        source='track.arrival_station.title'
    )

    class Meta:
        model = RouteItem
        fields = (
            'departure_station',
            'arrival_station',
        )


class RouteSerializer(serializers.ModelSerializer):
    items = RouteItemSerializer(many=True)
    trains = TrainSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'trains', 'items')

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
    train = serializers.SerializerMethodField()
    departure = serializers.SerializerMethodField()
    arrival = serializers.SerializerMethodField()

    class Meta:
        model = Ticket
        fields = ('train', 'departure', 'arrival')

    def get_train(self, obj):
        return (
            obj.ride.route.departure_station.title
            + ' -> '
            + obj.ride.route.arrival_station.title
        )

    def get_departure(self, obj):
        return (
            obj.ride.departure_date.strftime('%Y-%m-%d')
            + ' '
            + obj.ride.departure_time.strftime('%H:%M:%S')
        )

    def get_arrival(self, obj):
        return (
            obj.ride.arrival_date.strftime('%Y-%m-%d')
            + ' '
            + obj.ride.arrival_time.strftime('%H:%M:%S')
        )


class TicketBuySerializer(serializers.Serializer):
    ride_id = serializers.IntegerField()
    user_email = serializers.EmailField()

    def validate_ride_id(self, value):
        try:
            Ride.objects.get(id=value)
        except Ride.DoesNotExist:
            raise ValidationError('Ride with such id doesn\'t exist')

        return value

    def create(self, validated_data):
        ride = Ride.objects.get(id=validated_data['ride_id'])

        customer = User.objects.get(email=validated_data['user_email'])

        return Ticket.objects.create(customer=customer, ride=ride)


class RideSerializer(serializers.ModelSerializer):
    tickets = TicketSerializer(many=True, read_only=True)
    departure_station = serializers.ReadOnlyField(
        source='route.departure_station.title')
    arrival_station = serializers.ReadOnlyField(
        source='route.arrival_station.title')

    class Meta:
        model = Ride
        fields = (
            'id', 'route', 'amount',
            'departure_station', 'arrival_station',
            'departure_date', 'arrival_date',
            'departure_time', 'arrival_time',
            'tickets'
        )
        read_only_fields = ('amount',)

    def validate(self, attrs):
        if attrs['arrival_date'] <= attrs['departure_date']:
            raise ValidationError('Arrival cannot be after Departure')

        return attrs

    def create(self, validated_data):
        validated_data['amount'] = calculate_route_cost(validated_data['route'])

        return super().create(validated_data)

    def update(self, instance, validated_data):
        # if this ride's route is being changed
        # we need to recalculate its cost
        if instance.route != validated_data['route']:
            validated_data['amount'] = calculate_route_cost(validated_data['route'])

        return super().update(instance, validated_data)


class SpecificRideSerializer(serializers.ModelSerializer):
    items = RouteItemSerializer(
        source='route.items',
        many=True,
        required=False
    )
    departure_station = serializers.CharField(
        source='route.departure_station.title',
        required=True
    )
    arrival_station = serializers.CharField(
        source='route.arrival_station.title',
        required=True
    )

    class Meta:
        model = Ride
        fields = (
            'id', 'amount',
            'departure_station', 'arrival_station',
            'departure_date', 'arrival_date',
            'departure_time', 'arrival_time',
            'items'
        )
        read_only_fields = (
            'amount', 'arrival_date', 'departure_time',
            'arrival_time',
        )
