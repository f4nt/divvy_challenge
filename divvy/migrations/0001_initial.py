# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Station'
        db.create_table(u'divvy_station', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station_id', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'divvy', ['Station'])

        # Adding model 'Ride'
        db.create_table(u'divvy_ride', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('trip_id', self.gf('django.db.models.fields.IntegerField')()),
            ('start_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('end_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('bike', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['divvy.Bike'])),
            ('trip_duration', self.gf('django.db.models.fields.IntegerField')()),
            ('from_station', self.gf('django.db.models.fields.related.ForeignKey')(related_name='from_stop', to=orm['divvy.Station'])),
            ('to_station', self.gf('django.db.models.fields.related.ForeignKey')(related_name='to_station', to=orm['divvy.Station'])),
            ('user_type', self.gf('django.db.models.fields.CharField')(max_length=64)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=64, null=True, blank=True)),
            ('birth_year', self.gf('django.db.models.fields.CharField')(max_length=16, null=True, blank=True)),
        ))
        db.send_create_signal(u'divvy', ['Ride'])

        # Adding model 'Bike'
        db.create_table(u'divvy_bike', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bike_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'divvy', ['Bike'])


    def backwards(self, orm):
        # Deleting model 'Station'
        db.delete_table(u'divvy_station')

        # Deleting model 'Ride'
        db.delete_table(u'divvy_ride')

        # Deleting model 'Bike'
        db.delete_table(u'divvy_bike')


    models = {
        u'divvy.bike': {
            'Meta': {'object_name': 'Bike'},
            'bike_id': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'divvy.ride': {
            'Meta': {'object_name': 'Ride'},
            'bike': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['divvy.Bike']"}),
            'birth_year': ('django.db.models.fields.CharField', [], {'max_length': '16', 'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {}),
            'from_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'from_stop'", 'to': u"orm['divvy.Station']"}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {}),
            'to_station': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'to_station'", 'to': u"orm['divvy.Station']"}),
            'trip_duration': ('django.db.models.fields.IntegerField', [], {}),
            'trip_id': ('django.db.models.fields.IntegerField', [], {}),
            'user_type': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'divvy.station': {
            'Meta': {'object_name': 'Station'},
            'capacity': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'station_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['divvy']