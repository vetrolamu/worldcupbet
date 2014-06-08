# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Choice'
        db.delete_table(u'bets_choice')

        # Deleting model 'Poll'
        db.delete_table(u'bets_poll')


        # Changing field 'Game.visitor_ft_score'
        db.alter_column(u'bets_game', 'visitor_ft_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Game.home_et_score'
        db.alter_column(u'bets_game', 'home_et_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Game.visitor_pen_score'
        db.alter_column(u'bets_game', 'visitor_pen_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Game.home_ft_score'
        db.alter_column(u'bets_game', 'home_ft_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Game.visitor_et_score'
        db.alter_column(u'bets_game', 'visitor_et_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Game.home_pen_score'
        db.alter_column(u'bets_game', 'home_pen_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bet.visitor_ft_score'
        db.alter_column(u'bets_bet', 'visitor_ft_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bet.home_et_score'
        db.alter_column(u'bets_bet', 'home_et_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bet.visitor_pen_score'
        db.alter_column(u'bets_bet', 'visitor_pen_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bet.home_ft_score'
        db.alter_column(u'bets_bet', 'home_ft_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bet.home_pen_score'
        db.alter_column(u'bets_bet', 'home_pen_score', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Bet.visitor_et_score'
        db.alter_column(u'bets_bet', 'visitor_et_score', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):
        # Adding model 'Choice'
        db.create_table(u'bets_choice', (
            ('poll', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bets.Poll'])),
            ('choice_text', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('votes', self.gf('django.db.models.fields.IntegerField')(default=0)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'bets', ['Choice'])

        # Adding model 'Poll'
        db.create_table(u'bets_poll', (
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')()),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'bets', ['Poll'])


        # Changing field 'Game.visitor_ft_score'
        db.alter_column(u'bets_game', 'visitor_ft_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Game.home_et_score'
        db.alter_column(u'bets_game', 'home_et_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Game.visitor_pen_score'
        db.alter_column(u'bets_game', 'visitor_pen_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Game.home_ft_score'
        db.alter_column(u'bets_game', 'home_ft_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Game.visitor_et_score'
        db.alter_column(u'bets_game', 'visitor_et_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Game.home_pen_score'
        db.alter_column(u'bets_game', 'home_pen_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Bet.visitor_ft_score'
        db.alter_column(u'bets_bet', 'visitor_ft_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Bet.home_et_score'
        db.alter_column(u'bets_bet', 'home_et_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Bet.visitor_pen_score'
        db.alter_column(u'bets_bet', 'visitor_pen_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Bet.home_ft_score'
        db.alter_column(u'bets_bet', 'home_ft_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Bet.home_pen_score'
        db.alter_column(u'bets_bet', 'home_pen_score', self.gf('django.db.models.fields.IntegerField')(default=''))

        # Changing field 'Bet.visitor_et_score'
        db.alter_column(u'bets_bet', 'visitor_et_score', self.gf('django.db.models.fields.IntegerField')(default=''))

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
            'home_et_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'home_ft_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'home_pen_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'visitor_et_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'visitor_ft_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'visitor_pen_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'})
        },
        u'bets.game': {
            'Meta': {'object_name': 'Game'},
            'home': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'home'", 'null': 'True', 'to': u"orm['bets.Team']"}),
            'home_et_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'home_ft_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'home_pen_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.DateTimeField', [], {}),
            'visitor': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'visitor'", 'null': 'True', 'to': u"orm['bets.Team']"}),
            'visitor_et_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'visitor_ft_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'}),
            'visitor_pen_score': ('django.db.models.fields.IntegerField', [], {'default': "''", 'null': 'True'})
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