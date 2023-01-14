from rest_framework import serializers

from srijan_backend.apps.main.models.management import (
    Developers,
    Notification,
    OrganisingTeamMember,
)


class OrganisingTeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganisingTeamMember
        fields = "__all__"


class DevelopersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developers
        fields = "__all__"


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = "__all__"
