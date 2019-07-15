import itertools
from datetime import date, time

import yaml
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand, CommandError

from railways.models import (
    Ride,
    Route,
    RouteItem,
    Station,
    Ticket,
    Train,
    Track
)

from railways.utils import calculate_route_cost, get_logger

from users.models import User

logger = get_logger(filename='logs/generate_test_data.log')


class Command(BaseCommand):
    help = 'Generate test data for project\'s database'

    @staticmethod
    def generate_error_message(error_type, exception):
        return (
            'Cannot generate data. {} error: {}'.format(
                error_type,
                str(exception)
            )
        )

    @staticmethod
    def generate_stations():
        filename = 'test_data/stations.yaml'

        with open(filename, 'r') as file:
            test_data = yaml.load(file)

            for station in test_data['stations']:
                Station.objects.create(
                    title=station['title'],
                    country=station['country'],
                    latitude=station['latitude'],
                    longitude=station['longitude'],

                )

        logger.info('Stations generated.')

    @staticmethod
    def generate_users():
        filename = 'test_data/users.yaml'

        with open(filename, 'r') as file:
            test_data = yaml.load(file)
            for user in test_data['users']:
                User.objects.create(
                    email=user['email'],
                    first_name=user['first_name'],
                    last_name=user['last_name'],
                    password=make_password(user['password'])
                )

        logger.info('Users generated.')

    @staticmethod
    def generate_tracks():
        filename = 'test_data/tracks.yaml'

        with open(filename, 'r') as file:
            test_data = yaml.load(file)
            for track in test_data['tracks']:
                # create two-directional logical
                # track via two database tracks
                Track.objects.create(
                    departure_station=Station.objects.get(
                        title=track['departure_station']
                    ),
                    arrival_station=Station.objects.get(
                        title=track['arrival_station']
                    ),
                    length=track['length']
                )
                Track.objects.create(
                    departure_station=Station.objects.get(
                        title=track['arrival_station']
                    ),
                    arrival_station=Station.objects.get(
                        title=track['departure_station']
                    ),
                    length=track['length']
                )

        logger.info('Tracks generated.')

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
            Ticket.objects.create(
                customer=User.objects.get(email=ticket['customer']),
                ride=ride)

    @staticmethod
    def generate_rides(route, rides):
        for ride in rides:
            cost = calculate_route_cost(route)

            total_ride_length = 0
            for item in route.items.all():
                total_ride_length += item.track.length

            new_ride = Ride.objects.create(
                departure_date=date(*ride['departure_date']),
                departure_time=time(*ride['departure_time']),
                arrival_date=date(*ride['arrival_date']),
                arrival_time=time(*ride['arrival_time']),
                cost=cost,
                route=route
            )

            Command.generate_tickets(ride=new_ride, tickets=ride['tickets'])

    @staticmethod
    def generate_routes():
        filename = 'test_data/routes_rides_trains_tickets.yaml'

        with open(filename, 'r') as file:
            test_data = yaml.load(file)

            for route in test_data['routes']:
                # Route departure and arrival stations are
                # departure station of the first track in sequence and
                # arrival of the last.
                # Even if sequence consists of one track.
                new_route = Route.objects.create(
                    departure_station=Station.objects.get(
                        title=route['stations'][0]
                    ),
                    arrival_station=Station.objects.get(
                        title=route['stations'][-1]
                    )
                )

                Command.generate_train(route=new_route)

                Command.generate_route_items(
                    route=new_route,
                    stations=route['stations']
                )

                Command.generate_rides(
                    route=new_route,
                    rides=route['rides']
                )

        logger.info('Routes generated.')

    @staticmethod
    def generate_data():
        try:
            Command.generate_stations()
            Command.generate_users()
            Command.generate_tracks()
            Command.generate_routes()
        except yaml.YAMLError as e:
            logger.error(
                Command.generate_error_message('yaml', e)
            )
            raise CommandError(
                Command.generate_error_message('yaml', e)
            )

    @staticmethod
    def drop_database():
        logger.info('Start current database dropping...')

        # deleting all stations is enough to drop all data for now
        Station.objects.all().delete()
        User.objects.all().delete()

        logger.info('Database dropped.')

    def handle(self, *args, **options):
        print('Start generating...')
        logger.info('Start generating...')

        self.drop_database()
        self.generate_data()

        print('Done.')
        logger.info('Done.')
