from rest_framework import serializers

from srijan_backend.apps.main.models.activities import (
    Event,
    Exhibition,
    GuestTalk,
    Winner,
    Workshop,
)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Winner
        fields = "__all__"


class WorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"


class GuestTalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestTalk
        fields = "__all__"


class ExhibitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = "__all__"
