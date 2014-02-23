import csv

from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand

from divvy import models

DATE_FORMAT = '%Y-%m-%d %H:%M'


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fh = open('{}/Divvy_Trips_2013.csv'.format(settings.BASE_DIR))
        reader = csv.DictReader(fh)
        for row in reader:
            from_station_id = models.Station.objects.get(station_id=row['from_station_id']).pk
            to_station_id = models.Station.objects.get(station_id=row['to_station_id']).pk
            bike, created = models.Bike.objects.get_or_create(bike_id=row['bikeid'])
            models.Ride.objects.create(
                trip_id=row['trip_id'],
                trip_duration=row['tripduration'].replace(',', ''),
                gender=row['gender'],
                start_time=datetime.strptime(row['starttime'], DATE_FORMAT),
                end_time=datetime.strptime(row['stoptime'], DATE_FORMAT),
                user_type=row['usertype'],
                birth_year=row['birthday'],
                bike=bike, from_station_id=from_station_id, to_station_id=to_station_id
            )
