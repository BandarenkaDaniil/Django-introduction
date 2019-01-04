import csv
import itertools

from django.core.management.base import BaseCommand

from railways.models import Route
from railways.models import RouteItem
from railways.models import Station
from railways.models import Track
# from railways.models import Train


class Command(BaseCommand):
    help = 'Generate test data for project\'s database'

    def handle(self, *args, **options):
        # deleting all stations is enough to drop all data
        Station.objects.all().delete()

        filename = 'test_data/stations.csv'

        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                Station.objects.create(title=row[0], country=row[1])

        filename = 'test_data/tracks.csv'

        with open(filename) as f:
            reader = csv.reader(f)
            for row in reader:
                # create two-directional logical track via two database tracks
                Track.objects.create(
                    departure_station=Station.objects.get(title=row[0]),
                    arrival_station=Station.objects.get(title=row[1]),
                    length=row[2]
                )
                Track.objects.create(
                    departure_station=Station.objects.get(title=row[1]),
                    arrival_station=Station.objects.get(title=row[0]),
                    length=row[2]
                )

        filename = 'test_data/routes.csv'

        with open(filename) as f:
            reader = csv.reader(f)

            for row in reader:
                # Route departure and arrival stations are
                # departure station of the first track in sequence and
                # arrival of the last.
                # Even if sequence consists of one track.
                route = Route.objects.create(
                    departure_station=Station.objects.get(title=row[0]),
                    arrival_station=Station.objects.get(title=row[-1])
                )

                # form two independent iterators to get
                # tracks pairs like (1,2), (2,3), (3, 4) and so on
                iter1, iter2 = itertools.tee(row)
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
