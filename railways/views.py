from rest_framework import generics, permissions

from railways.serializers import \
    TrainSerializer, \
    StationSerializer, \
    RideSerializer

from railways.models import Train
from railways.models import Station
from railways.models import Ride

from railways.permissions import IsSuperUserOrReadOnly


class TrainList(generics.ListCreateAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TrainDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class StationList(generics.ListCreateAPIView):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RideList(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer
