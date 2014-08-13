# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'HttpRequestInfo.priority'
        db.add_column(u'http_storage_middleware_httprequestinfo', 'priority',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'HttpRequestInfo.priority'
        db.delete_column(u'http_storage_middleware_httprequestinfo', 'priority')


    models = {
        u'http_storage_middleware.httprequestinfo': {
            'Meta': {'object_name': 'HttpRequestInfo'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ajax': ('django.db.models.fields.BooleanField', [], {}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['http_storage_middleware']