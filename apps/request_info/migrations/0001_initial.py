# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models, DatabaseError


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestInfo'
        try:
            db.create_table(u'http_storage_middleware_httprequestinfo', (
                (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
                ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
                ('method', self.gf('django.db.models.fields.CharField')(max_length=10)),
                ('path', self.gf('django.db.models.fields.CharField')(max_length=150)),
                ('is_ajax', self.gf('django.db.models.fields.BooleanField')()),
            ))
            db.send_create_signal(u'http_storage_middleware', ['HttpRequestInfo'])
        except DatabaseError:
            pass


    def backwards(self, orm):
        # Deleting model 'HttpRequestInfo'
        db.delete_table(u'http_storage_middleware_httprequestinfo')


    models = {
        u'http_storage_middleware.httprequestinfo': {
            'Meta': {'object_name': 'HttpRequestInfo'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ajax': ('django.db.models.fields.BooleanField', [], {}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['http_storage_middleware']