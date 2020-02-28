from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.utils.text import slugify
from transliterate import translit
from django.urls import reverse


class Country(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    text = RichTextField()
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Tournament(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    text = RichTextField()
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Team(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    tournaments = models.ManyToManyField(Tournament)
    text = RichTextField()
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Player(models.Model):
    title = models.CharField(max_length=50)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, default=None)
    number = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    text = RichTextField()
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('player_detail', args=(self.slug,))


class Stadium(models.Model):
    title = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Referee(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.surname


class Match(models.Model):
    title = models.CharField(max_length=50)
    home_team = models.ForeignKey(Team, related_name='home_team', on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away_team', on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    score = models.CharField(max_length=10)
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    referee = models.ForeignKey(Referee, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    text = RichTextField()
    slug = models.SlugField(default='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class MatchResult(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class TeamInMatch(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    attempts = models.IntegerField(default=0)
    on_target = models.IntegerField(default=0)
    off_target = models.IntegerField(default=0)
    blocked = models.IntegerField(default=0)
    corners = models.IntegerField(default=0)
    offsides = models.IntegerField(default=0)
    ball_possession = models.IntegerField(default=0)
    pass_accuracy = models.IntegerField(default=0)
    passes = models.IntegerField(default=0)
    passes_completed = models.IntegerField(default=0)
    distance_covered = models.IntegerField(default=0)
    fouls_committed = models.IntegerField(default=0)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    match_result = models.ForeignKey(MatchResult, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.team.title


class PlayerInMatch(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    game_number = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(translit(instance.title, reversed=True))


pre_save.connect(slug_save, sender=Tournament)
pre_save.connect(slug_save, sender=Team)
pre_save.connect(slug_save, sender=Player)
pre_save.connect(slug_save, sender=Match)
