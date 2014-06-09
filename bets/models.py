from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Team(models.Model):
    name = models.CharField(max_length=200)
    short_name = models.CharField(max_length=3)
    def __unicode__(self):
        return self.name

class Game(models.Model):
    home = models.ForeignKey(Team, null=True, related_name='home')
    visitor = models.ForeignKey(Team, null=True, related_name='visitor')
    time = models.DateTimeField('game time')
    home_ft_score = models.CharField(max_length=3, null=True, blank=True)
    visitor_ft_score = models.CharField(max_length=3, null=True, blank=True)
    home_et_score = models.CharField(max_length=3, null=True, blank=True)
    visitor_et_score = models.CharField(max_length=3, null=True, blank=True)
    home_pen_score = models.CharField(max_length=3, null=True, blank=True)
    visitor_pen_score = models.CharField(max_length=3, null=True, blank=True)
    winner = models.CharField(max_length=1, null=True, blank=True)
    def __unicode__(self):
        return self.home.name + " - " + self.visitor.name

class Bet(models.Model):
    user = models.ForeignKey(User)
    game = models.ForeignKey(Game)
    time = models.DateTimeField(default=datetime.now, blank=True)
    home_ft_score = models.CharField(max_length=3, null=True, blank=True)
    visitor_ft_score = models.CharField(max_length=3, null=True, blank=True)
    home_et_score = models.CharField(max_length=3, null=True, blank=True)
    visitor_et_score = models.CharField(max_length=3, null=True, blank=True)
    home_pen_score = models.CharField(max_length=3, null=True, blank=True)
    visitor_pen_score = models.CharField(max_length=3, null=True, blank=True)
    winner = models.CharField(max_length=1, null=True, blank=True)
    def __unicode__(self):
        return self.user.username + ": " + str(self.game)