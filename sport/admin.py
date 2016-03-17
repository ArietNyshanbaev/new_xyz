from django.contrib import admin
from .models import Match, Bet

class MatchAdmin(admin.ModelAdmin):
	list_display = ('first_team_name', 'second_team_name', 'date')
	list_filter = ('date',)
admin.site.register(Match, MatchAdmin)

class BetAdmin(admin.ModelAdmin):
	list_display = ('user', 'date', 'over_all_result')
	list_filter = ('date', 'over_all_result')

admin.site.register(Bet, BetAdmin)