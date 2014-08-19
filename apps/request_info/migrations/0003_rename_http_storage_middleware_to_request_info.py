# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        db.rename_table(u'http_storage_middleware_httprequestinfo', u'request_info_httprequestinfo')

    def backwards(self, orm):
        db.rename_table(u'request_info_httprequestinfo', u'http_storage_middleware_httprequestinfo')

    models = {
        u'request_info.httprequestinfo': {
            'Meta': {'object_name': 'HttpRequestInfo'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_ajax': ('django.db.models.fields.BooleanField', [], {}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'path': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        }
    }

    complete_apps = ['request_info']