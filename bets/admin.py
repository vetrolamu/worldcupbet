from django.contrib import admin
from bets.models import Team, Game, Bet

admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Bet)