from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^matches/$', views.match_list, name='match_list'),
    re_path(r'^matches/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.match_detail, name='match_detail'),
    re_path(r'^players/$', views.player_list, name='player_list'),
    re_path(r'^players/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.player_detail, name='player_detail'),
    re_path(r'^tournaments/$', views.tournament_list, name='tournament_list'),
    re_path(r'^tournaments/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.tournament_detail, name='tournament_detail'),
    re_path(r'^teams/$', views.team_list, name='team_list'),
    re_path(r'^teams/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.team_detail, name='team_detail'),
]