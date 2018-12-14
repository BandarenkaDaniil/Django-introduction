from rest_framework import generics, permissions

from api.railways.serializers import (
    TrainSerializer,
    StationSerializer,
    RideSerializer
)

from railways.models import Train
from railways.models import Station
from railways.models import Ride

from railways.permissions import IsSuperUserOrReadOnly


class TrainListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TrainDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class StationListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RideListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer
