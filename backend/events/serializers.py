from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
  class Meta:
    model = Event
    fields = ['id','event_code','day','start','end','title', 'description','image','seats','max_seats', 'category','is_seminar', 'team_size', 'is_team_size_strict', 'entry_fee', 'prize_money']