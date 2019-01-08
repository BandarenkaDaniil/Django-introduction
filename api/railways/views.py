from rest_framework import generics, permissions
from rest_framework.response import Response

from api.railways.serializers import (
    RideSerializer,
    RouteSerializer,
    RouteItemSerializer,
    StationSerializer,
    TicketSerializer,
    TrainSerializer,
    TrackSerializer,
)

from railways.models import Ride
from railways.models import Route
from railways.models import RouteItem
from railways.models import Station
from railways.models import Ticket
from railways.models import Train
from railways.models import Track


class TrainListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class TrainDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Train.objects.all()
    serializer_class = TrainSerializer


class StationListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class StationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class TrackListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class RouteListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteItemListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = RouteItem.objects.all()
    serializer_class = RouteItemSerializer


class RouteItemDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = RouteItem.objects.all()
    serializer_class = RouteItemSerializer


class RideListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class RideDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Ride.objects.all()
    serializer_class = RideSerializer


class TicketListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
