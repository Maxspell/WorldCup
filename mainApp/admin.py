from django.contrib import admin
from .models import Country, Team, Tournament, Player, Match, Stadium, Referee, TeamInMatch, PlayerInMatch, MatchResult


class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = Country

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Country, CountryAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = Team

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Team, TeamAdmin)


class TournamentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = Tournament

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Tournament, TournamentAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'team', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = Player

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Player, PlayerAdmin)


class MatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'score', 'tournament', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = Match

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Match, MatchAdmin)


class StadiumAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = Stadium

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Stadium, StadiumAdmin)


class RefereeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'created', 'updated', 'user']
    list_display_links = ['name']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['name']

    class Meta:
        model = Referee

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(Referee, RefereeAdmin)


class TeamInMatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'team', 'match', 'goals_scored', 'goals_conceded', 'match_result', 'created', 'updated', 'user']
    list_display_links = ['team']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['team']

    class Meta:
        model = TeamInMatch

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(TeamInMatch, TeamInMatchAdmin)


class PlayerInMatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'player', 'match', 'created', 'updated', 'user']
    list_display_links = ['player']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['player']

    class Meta:
        model = PlayerInMatch

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(PlayerInMatch, PlayerInMatchAdmin)


class MatchResultAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created', 'updated', 'user']
    list_display_links = ['title']
    readonly_fields = ['created', 'updated', 'user']
    search_fields = ['title']

    class Meta:
        model = MatchResult

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'user', None) is None:
            obj.user = request.user
        obj.save()

admin.site.register(MatchResult, MatchResultAdmin)
