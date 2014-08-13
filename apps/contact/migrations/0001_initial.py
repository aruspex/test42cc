# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        pass
        # Adding model 'Person'
        # db.create_table(u'contact_person', (
        #     (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        #     ('surname', self.gf('django.db.models.fields.CharField')(max_length=25)),
        #     ('birth_date', self.gf('django.db.models.fields.DateField')()),
        #     ('bio', self.gf('django.db.models.fields.TextField')()),
        #     ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        #     ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        #     ('skype', self.gf('django.db.models.fields.CharField')(max_length=30)),
        #     ('other_contacts', self.gf('django.db.models.fields.TextField')()),
        # ))
        # db.send_create_signal(u'contact', ['Person'])


    def backwards(self, orm):
        # Deleting model 'Person'
        db.delete_table(u'contact_person')


    models = {
        u'contact.person': {
            'Meta': {'object_name': 'Person'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birth_date': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'surname': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        }
    }

    complete_apps = ['contact']