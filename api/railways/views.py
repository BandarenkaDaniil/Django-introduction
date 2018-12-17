from rest_framework import generics, permissions
from rest_framework.response import Response

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

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = TrainSerializer(queryset, many=True)
        return Response(serializer.data)


class TrainDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class StationListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)


class StationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class RideListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = RideSerializer(queryset, many=True)
        return Response(serializer.data)


class RideDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUserOrReadOnly,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer
