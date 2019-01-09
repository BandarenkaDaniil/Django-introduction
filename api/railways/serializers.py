import itertools

from rest_framework import serializers
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


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ('id', 'route')


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ('id', 'title', 'country')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('id', 'departure_station', 'arrival_station', 'length')


class RouteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteItem
        fields = ('track', )


class RouteSerializer(serializers.ModelSerializer):
    """TODO: add update method"""

    items = RouteItemSerializer(many=True)

    class Meta:
        model = Route
        fields = ('id', 'items', )

    @staticmethod
    def validate_items(attrs):
        """
            Checks if got tracks form correct sequence.
        """
        if not attrs:
            raise ValidationError("No tracks input")

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


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ('id', 'route', 'amount', 'departure_date', 'arrival_date', )


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'customer', 'ride')
