from django.http import JsonResponse

from rest_framework import generics, permissions
from rest_framework import views

from api.railways.serializers import (
    RideSerializer,
    SpecificRideSerializer,
    UserTicketsSerializer,
    RouteSerializer,
    RouteItemSerializer,
    StationSerializer,
    TicketSerializer,
    TicketBuySerializer,
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
    # permission_classes = (permissions.IsAuthenticated,)

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


class SpecificRidesAPI(generics.ListAPIView):
    serializer_class = SpecificRideSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        departure_station = Station.objects.get(title=self.request.query_params['departure_station'])
        arrival_station = Station.objects.get(title=self.request.query_params['arrival_station'])
        departure_date = self.request.query_params['departure_date']

        return Ride.objects.filter(departure_date=departure_date,
                                   route__departure_station=departure_station,
                                   route__arrival_station=arrival_station)


class TicketListAPI(generics.ListCreateAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class UserTicket(generics.ListAPIView):
    serializer_class = UserTicketsSerializer

    def get_queryset(self):
        return Ticket.objects.filter(customer=self.request.user)


class BuyTicket(views.APIView):
    def post(self, request):
        serializer = TicketBuySerializer(data=request.data)
        serializer.context['user'] = request.user
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(
            {'status': 'Ticket purchased'},
            status=201
        )


class TicketDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAdminUser,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
