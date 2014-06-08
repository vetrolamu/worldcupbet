# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'Bet', fields ['user']
        db.delete_unique(u'bets_bet', ['user_id'])

        # Removing unique constraint on 'Bet', fields ['game']
        db.delete_unique(u'bets_bet', ['game_id'])

        # Removing unique constraint on 'Game', fields ['home']
        db.delete_unique(u'bets_game', ['home_id'])

        # Removing unique constraint on 'Game', fields ['visitor']
        db.delete_unique(u'bets_game', ['visitor_id'])


        # Changing field 'Game.visitor'
        db.alter_column(u'bets_game', 'visitor_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bets.Team']))

        # Changing field 'Game.home'
        db.alter_column(u'bets_game', 'home_id', self.gf('django.db.models.fields.related.ForeignKey')(null=True, to=orm['bets.Team']))

        # Changing field 'Bet.game'
        db.alter_column(u'bets_bet', 'game_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bets.Game']))

        # Changing field 'Bet.user'
        db.alter_column(u'bets_bet', 'user_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']))

    def backwards(self, orm):

        # Changing field 'Game.visitor'
        db.alter_column(u'bets_game', 'visitor_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['bets.Team']))
        # Adding unique constraint on 'Game', fields ['visitor']
        db.create_unique(u'bets_game', ['visitor_id'])


        # Changing field 'Game.home'
        db.alter_column(u'bets_game', 'home_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['bets.Team']))
        # Adding unique constraint on 'Game', fields ['home']
        db.create_unique(u'bets_game', ['home_id'])


        # Changing field 'Bet.game'
        db.alter_column(u'bets_bet', 'game_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['bets.Game'], unique=True))
        # Adding unique constraint on 'Bet', fields ['game']
        db.create_unique(u'bets_bet', ['game_id'])


        # Changing field 'Bet.user'
        db.alter_column(u'bets_bet', 'user_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True))
        # Adding unique constraint on 'Bet', fields ['user']
        db.create_unique(u'bets_bet', ['user_id'])


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'bets.bet': {
            'Meta': {'object_name': 'Bet'},
            'game': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bets.Game']"}),
            'home_et_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'home_ft_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'home_pen_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'visitor_et_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'visitor_ft_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'visitor_pen_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'})
        },
        u'bets.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poll': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['bets.Poll']"}),
            'votes': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'bets.game': {
            'Meta': {'object_name': 'Game'},
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home'", 'null': 'True', 'to': u"orm['bets.Team']"}),
            'home_et_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'home_ft_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'home_pen_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'visitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitor'", 'null': 'True', 'to': u"orm['bets.Team']"}),
            'visitor_et_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'visitor_ft_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'}),
            'visitor_pen_score': ('django.db.models.fields.IntegerField', [], {'default': 'None'})
        },
        u'bets.poll': {
            'Meta': {'object_name': 'Poll'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'bets.team': {
            'Meta': {'object_name': 'Team'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['bets']