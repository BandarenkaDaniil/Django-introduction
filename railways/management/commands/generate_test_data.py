import pytz
import itertools
import yaml

from datetime import datetime

from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand

from railways.utils import calculate_amount

from railways.models import Ride
from railways.models import Route
from railways.models import RouteItem
from railways.models import Station
from railways.models import Ticket
from railways.models import Train
from railways.models import Track

from users.models import User


class Command(BaseCommand):
    help = 'Generate test data for project\'s database'

    @staticmethod
    def generate_stations():
        filename = 'test_data/stations.yaml'

        with open(filename, 'r') as file:
            try:
                test_data = yaml.load(file)
                for station in test_data['stations']:
                    Station.objects.create(title=station['title'],
                                           country=station['country'])
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def generate_users():
        filename = 'test_data/users.yaml'

        with open(filename, 'r') as file:
            try:
                test_data = yaml.load(file)
                for user in test_data['users']:
                    User.objects.create(email=user['email'],
                                        first_name=user['first_name'],
                                        last_name=user['last_name'],
                                        password=make_password(user['password']))
            except yaml.YAMLError as exc:
                print(exc)

        print('Stations generated.')

    @staticmethod
    def generate_tracks():
        filename = 'test_data/tracks.yaml'

        with open(filename, 'r') as file:
            try:
                test_data = yaml.load(file)
                for track in test_data['tracks']:
                    # create two-directional logical track via two database tracks
                    Track.objects.create(
                        departure_station=Station.objects.get(title=track['departure_station']),
                        arrival_station=Station.objects.get(title=track['arrival_station']),
                        length=track['length']
                    )
                    Track.objects.create(
                        departure_station=Station.objects.get(title=track['arrival_station']),
                        arrival_station=Station.objects.get(title=track['departure_station']),
                        length=track['length']
                    )
            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def generate_route_items(route, stations):
        # form two independent iterators to get
        # station pairs like (1,2), (2,3), (3, 4) and so on
        iter1, iter2 = itertools.tee(stations)
        next(iter2)

        station_pairs = list(zip(iter1, iter2))

        # previous item of the first route item
        # is always null
        previous_item = None

        for pair in station_pairs:
            item = RouteItem.objects.create(
                route=route,
                track=Track.objects.get(
                    departure_station=Station.objects.get(title=pair[0]),
                    arrival_station=Station.objects.get(title=pair[1])
                ),
                previous_item=previous_item
            )
            previous_item = item

    @staticmethod
    def generate_train(route):
        Train.objects.create(route=route)

    @staticmethod
    def generate_tickets(ride, tickets):
        for ticket in tickets:
            Ticket.objects.create(customer=User.objects.get(email=ticket['customer']),
                                  ride=ride)

    @staticmethod
    def generate_rides(route, rides):
        for ride in rides:
            amount = calculate_amount(route)

            new_ride = Ride.objects.create(
                departure_date=datetime(*ride['departure_date'], tzinfo=pytz.UTC),
                arrival_date=datetime(*ride['arrival_date'], tzinfo=pytz.UTC),
                amount=amount,
                route=route)

            Command.generate_tickets(ride=new_ride, tickets=ride['tickets'])

        print('Tracks generated.')

    @staticmethod
    def generate_routes():
        filename = 'test_data/routes_rides_trains_tickets.yaml'

        with open(filename, 'r') as file:
            try:
                test_data = yaml.load(file)

                for route in test_data['routes']:
                    # Route departure and arrival stations are
                    # departure station of the first track in sequence and
                    # arrival of the last.
                    # Even if sequence consists of one track.
                    new_route = Route.objects.create(
                        departure_station=Station.objects.get(title=route['stations'][0]),
                        arrival_station=Station.objects.get(title=route['stations'][-1])
                    )

                    Command.generate_train(route=new_route)

                    Command.generate_route_items(route=new_route, stations=route['stations'])

                    Command.generate_rides(route=new_route, rides=route['rides'])

            except yaml.YAMLError as exc:
                print(exc)

    @staticmethod
    def generate_data():
        Command.generate_stations()
        # Command.generate_users()
        Command.generate_tracks()
        Command.generate_routes()

        print('Routes generated.')

    def handle(self, *args, **options):
        print('Start generating...')

        # deleting all stations is enough to drop all data for now
        Station.objects.all().delete()
        # User.objects.all().delete()

        self.generate_data()

        print('Done.')






