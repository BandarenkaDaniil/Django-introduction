from django.http import JsonResponse

from rest_framework import generics, permissions
from rest_framework import views

from api.railways.serializers import (
    SpecificRideSerializer,
    UserTicketsSerializer,
    RouteSerializer,
    RouteItemSerializer,
    TicketSerializer,
    TicketBuySerializer,
)

from railways.models import (
    Ride,
    Route,
    RouteItem,
    Station,
    Ticket,
)


class RouteListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class RouteItemListAPI(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAdminUser,)

    queryset = RouteItem.objects.all()
    serializer_class = RouteItemSerializer


class SpecificRidesAPI(generics.ListAPIView):
    serializer_class = SpecificRideSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        departure_station = Station.objects.get(
            title=self.request.query_params.get('departure_station', None)
        )
        arrival_station = Station.objects.get(
            title=self.request.query_params.get('arrival_station', None)
        )
        departure_date = self.request.query_params.get('departure_date', None)

        return Ride.objects.filter(departure_date=departure_date,
                                   route__departure_station=departure_station,
                                   route__arrival_station=arrival_station)

    def list(self, request, *args, **kwargs):
        serializer = SpecificRideSerializer(data=request.query_params)

        serializer.is_valid(raise_exception=True)

        return super().list(request, *args, **kwargs)


class TicketListAPI(generics.ListCreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class UserTicket(generics.ListAPIView):
    serializer_class = UserTicketsSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Ticket.objects.filter(customer=self.request.user)


class BuyTicket(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        data = request.data.dict()

        data['user_email'] = request.user.email

        serializer = TicketBuySerializer(data=data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return JsonResponse(
            {'Purchase status': ['Success', ]},
            status=201
        )


class TicketDetailAPI(generics.RetrieveUpdateDestroyAPIView):

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
