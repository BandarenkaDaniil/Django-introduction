from rest_framework import generics, permissions
from rest_framework.response import Response

from api.railways.serializers import (
    # TrainSerializer,
    StationSerializer,
    TrackSerializer,
    RouteSerializer,
    RouteItemSerializer
)

# from railways.models import Train
from railways.models import Station
from railways.models import Track
from railways.models import Route
from railways.models import RouteItem


from railways.permissions import IsSuperUserOrReadOnly


# class TrainListAPI(generics.ListCreateAPIView):
#     permission_classes = (permissions.IsAuthenticated, )
#
#     queryset = Train.objects.all()
#     serializer_class = TrainSerializer
#
#     def get(self, request, *args, **kwargs):
#         super().get(request, *args, **kwargs)
#
#         queryset = self.get_queryset()
#         serializer = TrainSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#
# class TrainDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsSuperUserOrReadOnly, )
#
#     queryset = Train.objects.all()
#     serializer_class = TrainSerializer


class StationListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Station.objects.all()
    serializer_class = StationSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)


class StationDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Station.objects.all()
    serializer_class = StationSerializer


class TrackListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Track.objects.all()
    serializer_class = TrackSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = TrackSerializer(queryset, many=True)
        return Response(serializer.data)


class TrackDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsSuperUserOrReadOnly, )

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class RouteListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = RouteSerializer(queryset, many=True)
        return Response(serializer.data)


class RouteDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsSuperUserOrReadOnly,)

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteItemListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAuthenticated,)

    queryset = RouteItem.objects.all()
    serializer_class = RouteItemSerializer

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        queryset = self.get_queryset()
        serializer = RouteItemSerializer(queryset, many=True)
        return Response(serializer.data)


class RouteItemDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsSuperUserOrReadOnly,)

    queryset = RouteItem.objects.all()
    serializer_class = RouteItemSerializer
