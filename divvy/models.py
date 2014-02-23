from django.db import models


class Station(models.Model):

    station_id = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    slug = models.SlugField()
    latitude = models.CharField(max_length=64, null=True, blank=True)
    longitude = models.CharField(max_length=64, null=True, blank=True)
    capacity = models.IntegerField(null=True)
    online_date = models.DateField(null=True)
    landmark = models.CharField(max_length=128, blank=True, null=True)

    def __unicode__(self):
        return u'{}'.format(self.name)


class Bike(models.Model):

    bike_id = models.IntegerField()


class Ride(models.Model):

    trip_id = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    bike = models.ForeignKey('Bike')
    trip_duration = models.IntegerField()
    from_station = models.ForeignKey('Station', related_name='from_stop')
    to_station = models.ForeignKey('Station', related_name='to_station')
    user_type = models.CharField(max_length=64)
    gender = models.CharField(max_length=64, blank=True, null=True)
    birth_year = models.CharField(max_length=16, blank=True, null=True)
