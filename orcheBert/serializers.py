from rest_framework import serializers
from .models import orcheBert, Humming_MIDI, OrchestraMIDI


class GetHummingMIDISerializer(serializers.ModelSerializer):
    class Meta:
        model = OrchestraMIDI
        fields = ('id', 'title', 'file_path', 'owner', 'created_at', 'humming_midi')