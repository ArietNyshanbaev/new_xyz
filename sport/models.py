from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

class Match(models.Model):

    first_team_name = models.CharField('первая команда', max_length=100)
    second_team_name = models.CharField('вторая команда', max_length=100)
    result = models.IntegerField('результат', null=True, blank=True)
    first_team_score = models.IntegerField('забила первая команда', default=0)
    second_team_score = models.IntegerField('забила вторая команда', default=0)
    date = models.DateTimeField('дата матча', default=datetime.now())

    def __unicode__(self):
        return self.first_team_name + " vs " + self.second_team_name

    class Meta:
        verbose_name = "матч"
        verbose_name_plural = "матчи"


class Bet(models.Model):

    user = models.ForeignKey(User, verbose_name='пользователь ')
    date = models.DateTimeField('Время создания ', default=datetime.now)
    match1 = models.ForeignKey(Match, related_name='match1')
    match2 = models.ForeignKey(Match, related_name='match2')
    match3 = models.ForeignKey(Match, related_name='match3')
    match4 = models.ForeignKey(Match, related_name='match4')
    match5 = models.ForeignKey(Match, related_name='match5')
    match6 = models.ForeignKey(Match, related_name='match6')
    match7 = models.ForeignKey(Match, related_name='match7')
    match8 = models.ForeignKey(Match, related_name='match8')
    match9 = models.ForeignKey(Match, related_name='match9')
    match10 = models.ForeignKey(Match, related_name='match10')
    
    match1_prediction = models.IntegerField(default=0)
    match2_prediction = models.IntegerField(default=0)
    match3_prediction = models.IntegerField(default=0)
    match4_prediction = models.IntegerField(default=0)
    match5_prediction = models.IntegerField(default=0)
    match6_prediction = models.IntegerField(default=0)
    match7_prediction = models.IntegerField(default=0)
    match8_prediction = models.IntegerField(default=0)
    match9_prediction = models.IntegerField(default=0)
    match10_prediction = models.IntegerField(default=0)

    match1_result = models.BooleanField(default=False)
    match2_result = models.BooleanField(default=False)
    match3_result = models.BooleanField(default=False)
    match4_result = models.BooleanField(default=False)
    match5_result = models.BooleanField(default=False)
    match6_result = models.BooleanField(default=False)
    match7_result = models.BooleanField(default=False)
    match8_result = models.BooleanField(default=False)
    match9_result = models.BooleanField(default=False)
    match10_result = models.BooleanField(default=False)

    over_all_result = models.IntegerField(default=0);

    date_modified = models.DateTimeField('Дата последних изменений', default=datetime.now())
    
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = "ставка"
        verbose_name_plural = "ставки"