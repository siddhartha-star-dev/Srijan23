from django.contrib import admin

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


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "presented_by")


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ("name", "event", "position")


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(GuestTalk)
class GuestTalkAdmin(admin.ModelAdmin):
    list_display = ("guest_name",)


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(OrganisingTeamMember)
class OrganisingTeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "contact")


@admin.register(Developers)
class DevelopersAdmin(admin.ModelAdmin):
    list_display = ("name", "contact")


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ("title", "timestamp")


@admin.register(Merchandise)
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ("name", "price")
