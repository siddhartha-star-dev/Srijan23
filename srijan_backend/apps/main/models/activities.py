from django.db import models
from django.utils.translation import gettext_lazy as _


class EventType(models.TextChoices):
    DEPARTMENTAL = "departmental", _("Departmetal")
    INFORMAL = "informal", _("Informal")
    CLUB = "club", _("Club")


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    presented_by = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    details = models.TextField()
    event_type = models.CharField(choices=EventType.choices, max_length=20)
    brochure_link = models.URLField()
    register_link = models.URLField()
    image = models.ImageField(upload_to="event_images")
    register_timestamp = models.DateTimeField()
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    event_complete = models.BooleanField(default=False)
    venue = models.CharField(max_length=100)


class Winner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    position = models.IntegerField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


class Workshop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    details = models.TextField()
    register_link = models.URLField()
    image = models.ImageField(upload_to="workshop_images")
    register_timestamp = models.DateTimeField()
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    details = models.TextField()
    image = models.ImageField(upload_to="exhibition_images")
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class GuestTalk(models.Model):
    id = models.IntegerField(primary_key=True)
    guest_name = models.CharField(max_length=100)
    summary = models.CharField(max_length=250)
    details = models.TextField()
    register_link = models.URLField()
    image = models.ImageField(upload_to="guest_images")
    register_timestamp = models.DateTimeField()
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()
    venue = models.CharField(max_length=100)

    def __str__(self):
        return self.guest_name
