from rest_framework import serializers

from railways.models import Train
from railways.models import Station
from railways.models import Ride


class TrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ('id', 'type', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at', )


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = (
            'id', 'title', 'country', 'longitude',
            'latitude', 'created_at', 'updated_at'
        )
        read_only_fields = (
            'id', 'longitude', 'latitude',
            'created_at', 'updated_at',
        )


class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = (
            'id', 'user', 'train', 'departure_station',
            'arrival_station', 'created_at', 'updated_at'
        )
        read_only_fields = ('id', 'created_at', 'updated_at',)
