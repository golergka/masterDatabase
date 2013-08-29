# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Service'
        db.create_table(u'masterCollection_service', (
            ('url_name', self.gf('django.db.models.fields.SlugField')(max_length=50, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'masterCollection', ['Service'])

        # Adding model 'Master'
        db.create_table(u'masterCollection_master', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=254)),
        ))
        db.send_create_signal(u'masterCollection', ['Master'])

        # Adding model 'MasterService'
        db.create_table(u'masterCollection_masterservice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('master', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['masterCollection.Master'])),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['masterCollection.Service'])),
            ('price', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'masterCollection', ['MasterService'])

        # Adding unique constraint on 'MasterService', fields ['master', 'service']
        db.create_unique(u'masterCollection_masterservice', ['master_id', 'service_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'MasterService', fields ['master', 'service']
        db.delete_unique(u'masterCollection_masterservice', ['master_id', 'service_id'])

        # Deleting model 'Service'
        db.delete_table(u'masterCollection_service')

        # Deleting model 'Master'
        db.delete_table(u'masterCollection_master')

        # Deleting model 'MasterService'
        db.delete_table(u'masterCollection_masterservice')


    models = {
        u'masterCollection.master': {
            'Meta': {'object_name': 'Master'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'services': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['masterCollection.Service']", 'through': u"orm['masterCollection.MasterService']", 'symmetrical': 'False'})
        },
        u'masterCollection.masterservice': {
            'Meta': {'unique_together': "(('master', 'service'),)", 'object_name': 'MasterService'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'master': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['masterCollection.Master']"}),
            'price': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['masterCollection.Service']"})
        },
        u'masterCollection.service': {
            'Meta': {'object_name': 'Service'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url_name': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'primary_key': 'True'})
        }
    }

    complete_apps = ['masterCollection']