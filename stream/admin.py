from django.contrib import admin
from stream.models import Game, Stream


class GameAdmin(admin.ModelAdmin):
  list_display = ('title', 'code')


class StreamAdmin(admin.ModelAdmin):
  fieldsets = [
    (None,  {'fields': ['date', 'day_off']}),
    (None,  {'fields': ['featured_game', 'start', 'end', 'description']}),
  ]
  list_display = ('date', 'start', 'end', 'featured_game')


admin.site.register(Game, GameAdmin)
admin.site.register(Stream, StreamAdmin)