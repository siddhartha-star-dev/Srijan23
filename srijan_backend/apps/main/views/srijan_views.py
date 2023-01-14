from drf_psq import PsqMixin, Rule
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from srijan_backend.apps.main.models import (
    Developers,
    Event,
    Exhibition,
    GuestTalk,
    Merchandise,
    Notification,
    OrganisingTeamMember,
    Sponsor,
    Winner,
    Workshop,
)
from srijan_backend.apps.main.serializers import (
    DevelopersSerializer,
    EventSerializer,
    ExhibitionSerializer,
    GuestTalkSerializer,
    MerchandiseSerializer,
    NotificationSerializer,
    OrganisingTeamMemberSerializer,
    SponsorSerializer,
    WinnerSerializer,
    WorkshopSerializer,
)


class EventViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], EventSerializer)],
        "retrieve": [Rule([AllowAny], EventSerializer)],
    }

    def get_queryset(self):
        return Event.objects.filter(to_publish=True)


class ExhibitionViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], ExhibitionSerializer)],
        "retrieve": [Rule([AllowAny], ExhibitionSerializer)],
    }

    def get_queryset(self):
        return Exhibition.objects.all()


class GuestTalkViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], GuestTalkSerializer)],
        "retrieve": [Rule([AllowAny], GuestTalkSerializer)],
    }

    def get_queryset(self):
        return GuestTalk.objects.all()


class MerchandiseViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], MerchandiseSerializer)],
        "retrieve": [Rule([AllowAny], MerchandiseSerializer)],
    }

    def get_queryset(self):
        return Merchandise.objects.all()


class NotificationViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], NotificationSerializer)],
        "retrieve": [Rule([AllowAny], NotificationSerializer)],
    }

    def get_queryset(self):
        return Notification.objects.all()


class OrganisingTeamMemberViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], OrganisingTeamMemberSerializer)],
        "retrieve": [Rule([AllowAny], OrganisingTeamMemberSerializer)],
    }

    def get_queryset(self):
        return OrganisingTeamMember.objects.all()


class DevelopersViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], DevelopersSerializer)],
        "retrieve": [Rule([AllowAny], DevelopersSerializer)],
    }

    def get_queryset(self):
        return Developers.objects.all()


class SponsorViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], SponsorSerializer)],
        "retrieve": [Rule([AllowAny], SponsorSerializer)],
    }

    def get_queryset(self):
        return Sponsor.objects.all()


class WinnerViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], WinnerSerializer)],
        "retrieve": [Rule([AllowAny], WinnerSerializer)],
    }

    def get_queryset(self):
        return Winner.objects.all()


class WorkshopViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    PsqMixin,
    GenericViewSet,
):
    http_method_names = [
        "get",
    ]
    pagination_class = None
    permission_classes = [AllowAny]
    psq_rules = {
        "list": [Rule([AllowAny], WorkshopSerializer)],
        "retrieve": [Rule([AllowAny], WorkshopSerializer)],
    }

    def get_queryset(self):
        return Workshop.objects.all()
