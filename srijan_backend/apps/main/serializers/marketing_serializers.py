from rest_framework import serializers

from srijan_backend.apps.main.models.marketing import Merchandise, Sponsor


class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = "__all__"


class MerchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchandise
        fields = "__all__"
