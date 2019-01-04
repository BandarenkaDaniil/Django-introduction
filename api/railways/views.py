from rest_framework import generics, permissions
from rest_framework.response import Response

from api.railways.serializers import (
    RouteSerializer,
    RouteItemSerializer,
    StationSerializer,
    TrackSerializer,
    # TrainSerializer,
)

from railways.models import Route
from railways.models import RouteItem
from railways.models import Station
from railways.models import Track
# from railways.models import Train


# class TrainListAPI(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     queryset = Train.objects.all()
#     serializer_class = TrainSerializer
#
#
# class TrainDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
#
#     queryset = Train.objects.all()
#     serializer_class = TrainSerializer


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
