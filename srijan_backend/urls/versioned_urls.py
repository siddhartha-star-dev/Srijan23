from django.urls import include, path
from rest_framework.routers import SimpleRouter

from srijan_backend.apps.accounts.views import ProfileViewSet
from srijan_backend.apps.main.views import (
    EventViewSet,
    ExhibitionViewSet,
    GuestTalkViewSet,
    MerchandiseViewSet,
    NotificationViewSet,
    OrganisingTeamMemberViewSet,
    SponsorViewSet,
    WinnerViewSet,
    WorkshopViewSet,
)

router = SimpleRouter()
router.register("profiles", ProfileViewSet, basename="profile")
router.register("events", EventViewSet, basename="event")
router.register("exhibitions", ExhibitionViewSet, basename="exhibition")
router.register("guesttalks", GuestTalkViewSet, basename="guesttalk")
router.register("merchandises", MerchandiseViewSet, basename="merchandise")
router.register("notifications", NotificationViewSet, basename="notification")
router.register(
    "organisingteammembers",
    OrganisingTeamMemberViewSet,
    basename="organisingteammember",
)
router.register("sponsors", SponsorViewSet, basename="sponsor")
router.register("winners", WinnerViewSet, basename="winner")
router.register("workshops", WorkshopViewSet, basename="workshop")

versioned_urls = [path("", include(router.urls))]
