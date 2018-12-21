from rest_framework import serializers

# from railways.models import Train
from railways.models import Station
from railways.models import Track
from railways.models import Route
from railways.models import RouteItem


# class TrainSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Train
#         fields = ('id', 'type', 'created_at', 'updated_at')
#         read_only_fields = ('id', 'created_at', 'updated_at', )


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
            'id', 'title', 'country', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at',
        )


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = (
            'id', 'departure_station', 'arrival_station',
            'length', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'id', 'created_at', 'updated_at',
        )


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = (
            'id', 'departure_station', 'arrival_station',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at',)


class RouteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteItem
        fields = (
            'id', 'route', 'track', 'previous_item',
            'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at',)
