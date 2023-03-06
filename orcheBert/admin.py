from django.contrib import admin
from .models import orcheBert, Users, Humming_MIDI, OrchestraMIDI, Favorite


admin.site.register(orcheBert)
admin.site.register(Users)
admin.site.register(Humming_MIDI)
admin.site.register(OrchestraMIDI)
admin.site.register(Favorite)