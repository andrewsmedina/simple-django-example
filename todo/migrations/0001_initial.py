# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Todo'
        db.create_table(u'todo_todo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'todo', ['Todo'])


    def backwards(self, orm):
        # Deleting model 'Todo'
        db.delete_table(u'todo_todo')


    models = {
        u'todo.todo': {
            'Meta': {'object_name': 'Todo'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['todo']