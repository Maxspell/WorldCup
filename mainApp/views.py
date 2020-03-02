from django.shortcuts import render, get_object_or_404
from django.db.models import Count, Sum, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import urllib.request
import json
from .models import Tournament, Team, Player, Match, TeamInMatch, PlayerInMatch


def index(request):
    matches = Match.objects.all()[:5]
    teams = Team.objects.annotate(count_matches=Count('teaminmatch'),
                                 goals_scored=Sum('teaminmatch__goals_scored'),
                                 goals_conceded=Sum('teaminmatch__goals_conceded'),
                                 difference=Sum('teaminmatch__goals_scored') - Sum('teaminmatch__goals_conceded'),
                                 win_count=Count('teaminmatch', filter=Q(teaminmatch__match_result_id=1)),
                                 draw_count=Count('teaminmatch', filter=Q(teaminmatch__match_result_id=2)),
                                 loss_count=Count('teaminmatch', filter=Q(teaminmatch__match_result_id=3)),
                                 points=(Count('teaminmatch', filter=Q(teaminmatch__match_result_id=1)) * 3) +
                                        (Count('teaminmatch', filter=Q(teaminmatch__match_result_id=2)))
                                 ).order_by('-points')[:5]
    players = Player.objects.annotate(count_matches=Count('playerinmatch'),
                                      goals=Sum('playerinmatch__goals')).order_by('-goals')[:5]
    tournaments = Tournament.objects.all()[:5]
    context = {
        'matches': matches,
        'teams': teams,
        'players': players,
        'tournaments': tournaments
    }
    return render(request, 'mainApp/index.html', context)


def tournament_list(request):
    list = Tournament.objects.all()
    paginator = Paginator(list, 5)
    page = request.GET.get('page')
    tournaments = paginator.get_page(page)
    context = {
        'tournament_list': tournaments
    }
    return render(request, 'mainApp/tournament_list.html', context)


def tournament_detail(request, pk, slug):
    tournament = get_object_or_404(Tournament, pk=pk)
    context = {
        'tournament': tournament
    }
    return render(request, 'mainApp/tournament_detail.html', context)


def team_list(request):
    list = Team.objects.annotate(count_matches=Count('teaminmatch'),
                                 goals_scored=Sum('teaminmatch__goals_scored'),
                                 goals_conceded=Sum('teaminmatch__goals_conceded'),
                                 difference=Sum('teaminmatch__goals_scored') - Sum('teaminmatch__goals_conceded'),
                                 win_count=Count('teaminmatch', filter=Q(teaminmatch__match_result_id=1)),
                                 draw_count=Count('teaminmatch', filter=Q(teaminmatch__match_result_id=2)),
                                 loss_count=Count('teaminmatch', filter=Q(teaminmatch__match_result_id=3)),
                                 points=(Count('teaminmatch', filter=Q(teaminmatch__match_result_id=1)) * 3) +
                                        (Count('teaminmatch', filter=Q(teaminmatch__match_result_id=2)))
                                 ).order_by('-points')
    paginator = Paginator(list, 50)
    page = request.GET.get('page')
    teams = paginator.get_page(page)
    context = {
        'team_list': teams
    }
    return render(request, 'mainApp/team_list.html', context)


def team_detail(request, pk, slug):
    team = get_object_or_404(Team, pk=pk)
    context = {
        'team': team
    }
    return render(request, 'mainApp/team_detail.html', context)


def player_list(request):
    list = Player.objects.annotate(count_matches=Count('playerinmatch'),
                                   goals=Sum('playerinmatch__goals')).order_by('-goals')
    paginator = Paginator(list, 20)
    page = request.GET.get('page')
    players = paginator.get_page(page)
    context = {
        'player_list': players
    }
    return render(request, 'mainApp/player_list.html', context)


def player_detail(request, pk, slug):
    player = get_object_or_404(Player, pk=pk)
    context = {
        'player': player
    }
    return render(request, 'mainApp/player_detail.html', context)


def match_list(request):
    list = Match.objects.all()
    paginator = Paginator(list, 10)
    page = request.GET.get('page')
    matches = paginator.get_page(page)
    context = {
        'matches_list': matches
    }
    return  render(request, 'mainApp/match_list.html', context)


def match_detail(request, pk, slug):
    match = get_object_or_404(Match, pk=pk)
    home_match_statistics = TeamInMatch.objects.filter(match=pk, team=match.home_team)
    away_match_statistics = TeamInMatch.objects.filter(match=pk, team=match.away_team)
    home_team_players = PlayerInMatch.objects.filter(match=pk, player__team=match.home_team)
    away_team_players = PlayerInMatch.objects.filter(match=pk, player__team=match.away_team)
    context = {
        'match': match,
        'home_match_statistics': home_match_statistics,
        'away_match_statistics': away_match_statistics,
        'home_team_players': home_team_players,
        'away_team_players': away_team_players
    }
    return  render(request, 'mainApp/match_detail.html', context)


