import csv

from datetime import datetime

from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand

from divvy import models

DATE_FORMAT = '%m/%d/%Y'


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        fh = open('{}/Divvy_Stations_2013.csv'.format(settings.BASE_DIR))
        reader = csv.DictReader(fh)
        for row in reader:
            models.Station.objects.get_or_create(
                station_id=row['id'],
                latitude=row['latitude'],
                longitude=row['longitude'],
                capacity=row['dpcapacity'],
                landmark=row['landmark'],
                online_date=datetime.strptime(row['online date'], DATE_FORMAT),
                name=row['name'],
                slug=slugify(row['name']),
            )
