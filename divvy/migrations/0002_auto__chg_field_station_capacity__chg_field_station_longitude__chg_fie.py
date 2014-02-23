# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Station.capacity'
        db.alter_column(u'divvy_station', 'capacity', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Station.longitude'
        db.alter_column(u'divvy_station', 'longitude', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

        # Changing field 'Station.latitude'
        db.alter_column(u'divvy_station', 'latitude', self.gf('django.db.models.fields.CharField')(max_length=64, null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Station.capacity'
        raise RuntimeError("Cannot reverse this migration. 'Station.capacity' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Station.capacity'
        db.alter_column(u'divvy_station', 'capacity', self.gf('django.db.models.fields.IntegerField')())

        # User chose to not deal with backwards NULL issues for 'Station.longitude'
        raise RuntimeError("Cannot reverse this migration. 'Station.longitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Station.longitude'
        db.alter_column(u'divvy_station', 'longitude', self.gf('django.db.models.fields.CharField')(max_length=64))

        # User chose to not deal with backwards NULL issues for 'Station.latitude'
        raise RuntimeError("Cannot reverse this migration. 'Station.latitude' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Station.latitude'
        db.alter_column(u'divvy_station', 'latitude', self.gf('django.db.models.fields.CharField')(max_length=64))

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
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'station_id': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['divvy']