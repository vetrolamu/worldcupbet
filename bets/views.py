from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from bets.models import Bet, Team, Game
from django.contrib.auth.decorators import login_required
from django.utils.timezone import utc
import time
import pytz
from django.http import Http404
from django.contrib.auth.models import User
from django.conf import settings

from datetime import datetime

local_tz = pytz.timezone('Europe/Moscow') # use your local timezone name here
# Create your views here.

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    return local_tz.normalize(local_dt) # .normalize might be unnecessary

def get_score(bet, game):
    bonus_points = 0
    try:
        if game.id > settings.GROUP_GAMES:
            bet.winner = int(bet.winner)
            game.winner = int(game.winner)
            if bet.winner == game.winner:
                bonus_points = settings.BONUS_POINTS
            else:
                bonus_points = 0
    except:
        bonus_points = 0
    try:
        bet.home_ft_score = int(bet.home_ft_score)
        bet.visitor_ft_score = int(bet.visitor_ft_score)
        game.home_ft_score = int(game.home_ft_score)
        game.visitor_ft_score = int(game.visitor_ft_score)
    except:
        return settings.INCORRECT_RESULT + bonus_points

    if bet.home_ft_score == game.home_ft_score and bet.visitor_ft_score == game.visitor_ft_score:
        return settings.CORRECT_SCORE + bonus_points

    if bet.home_ft_score - bet.visitor_ft_score == game.home_ft_score - game.visitor_ft_score:
        return settings.CORRECT_DIFFERENCE + bonus_points

    if (bet.home_ft_score > bet.visitor_ft_score) * (game.home_ft_score > game.visitor_ft_score):
        return settings.CORRECT_RESULT + bonus_points
    else:
        return settings.INCORRECT_RESULT + bonus_points


def get_user_stats(me, user, games):
    user_bets = []
    overall_score = 0
    for game in games:

        game.local_time = utc_to_local(game.time)
        game.started = is_time_gone(game.local_time)
        game.display_time = game.local_time.strftime('%d.%m.%Y %H:%M')

        start_time = datetime(2012, 3, 1, 10, 0).replace(tzinfo=utc)
        try:
            user_bet = Bet.objects.filter(game=game, user=user, time__range=(start_time, game.time)).last()
        except:
            user_bet = None
        if user == me:
            show_bet = True
        else:
            show_bet = game.started

        score = get_score(user_bet, game)

        user_bets.append({
            "bet": user_bet,
            "game": game,
            "score": score,
            "show_bet": show_bet,
            "show_link": not game.started
        })
        overall_score += score

    user_groups = user.groups.values_list('name', flat=True)

    return {"user": user, "user_groups": user_groups, "user_bets": user_bets, "overall_score": overall_score}


def is_time_gone(input_time):
    current_time = utc_to_local(datetime.utcnow())
    if current_time > input_time:
        return True
    else:
        return False



@login_required
def index(request):

    current_time = time.localtime()
    games = Game.objects.order_by('time')

    user_stats = get_user_stats(request.user, request.user, games)


    for game in games:
        game.time = utc_to_local(game.time)
        game.display_time = game.time.strftime('%d.%m.%Y %H:%M')
        try:
            game.my_bet = Bet.objects.filter(game = game, user = request.user).last()
        except:
            game.my_bet = None

    current_time = time.strftime('%d.%m.%Y %H:%M:%S', current_time)
    context = RequestContext(request, {
        'page' : 'index',
        'user_stats': user_stats,
        'GROUP_GAMES': settings.GROUP_GAMES,
        'current_time': current_time
    })
    return render(request, 'bets/index.html', context)


@login_required
def overall(request):

    games = Game.objects.order_by('time')
    users = User.objects.exclude(groups__name = "disabled").order_by("groups")

    all_users_stats = []

    for user in users:
        all_users_stats.append(get_user_stats(request.user, user, games))

    context = RequestContext(request, {
        'page' : 'overall',
        'games': games,
        'all_users_stats': all_users_stats,
        'GROUP_GAMES': settings.GROUP_GAMES,
        'me': request.user
    })
    return render(request, 'bets/overall.html', context)

@login_required
def rules(request):

    context = RequestContext(request, {
        'page' : 'rules'
    })
    return render(request, 'bets/rules.html', context)


@login_required
def save_bet(request, game_id):

    new_bet = Bet()

    game = Game.objects.get(pk=request.POST["game"])
    user = request.user

    new_bet.game = game
    new_bet.user = user


    try:
        new_bet.home_ft_score = request.POST["home_ft_score"]
    except:
        new_bet.home_ft_score = None
    try:
        new_bet.visitor_ft_score = request.POST["visitor_ft_score"]
    except:
        new_bet.visitor_ft_score = None
    try:
        new_bet.home_et_score = request.POST["home_et_score"]
    except:
        new_bet.home_et_score = None
    try:
        new_bet.visitor_et_score = request.POST["visitor_et_score"]
    except:
        new_bet.visitor_et_score = None
    try:
        new_bet.home_pen_score = request.POST["home_pen_score"]
    except:
        new_bet.home_pen_score = None
    try:
        new_bet.visitor_pen_score = request.POST["visitor_pen_score"]
    except:
        new_bet.visitor_pen_score = None
    try:
        new_bet.winner = request.POST["winner"]
    except:
        new_bet.winner = None

    new_bet.save()

    return HttpResponseRedirect("/")


@login_required
def save_game_score(request, game_id):


    game = Game.objects.get(pk=request.POST["game"])

    try:
        game.home_ft_score = request.POST["home_ft_score"]
    except:
        game.home_ft_score = None
    try:
        game.visitor_ft_score = request.POST["visitor_ft_score"]
    except:
        game.visitor_ft_score = None
    try:
        game.home_et_score = request.POST["home_et_score"]
    except:
        game.home_et_score = None
    try:
        game.visitor_et_score = request.POST["visitor_et_score"]
    except:
        game.visitor_et_score = None
    try:
        game.home_pen_score = request.POST["home_pen_score"]
    except:
        game.home_pen_score = None
    try:
        game.visitor_pen_score = request.POST["visitor_pen_score"]
    except:
        game.visitor_pen_score = None
    try:
        game.winner = request.POST["winner"]
    except:
        game.winner = None

    game.save()

    return HttpResponseRedirect("/")



@login_required
def bet(request, game_id):
    user = request.user
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404

    try:
        bets = Bet.objects.filter(game_id=game_id, user=user)
        existing_bet = bets.last()
    except:
        existing_bet = None

    context = RequestContext(request, {
        'game': game,
        'GROUP_GAMES': settings.GROUP_GAMES,
        'existing_bet': existing_bet,
        'is_available': not is_time_gone(utc_to_local(game.time))

    })
    return render(request, 'bets/bet.html', context)
@login_required


def game_score(request, game_id):
    user = request.user
    try:
        game = Game.objects.get(pk=game_id)
    except Game.DoesNotExist:
        raise Http404

    context = RequestContext(request, {
        'game': game,
        'GROUP_GAMES': settings.GROUP_GAMES,
        'is_available': is_time_gone(utc_to_local(game.time))

    })
    return render(request, 'bets/game-score.html', context)