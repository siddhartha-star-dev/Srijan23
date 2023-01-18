from django.db import models
from django.utils.translation import gettext_lazy as _


class SponsorType(models.TextChoices):
    TITLE = "title", _("Title")
    DECORATION = "decoration", _("Decoration")
    ASSOCIATE = "associate", _("Associate")
    STRATEGIC = "strategic", _("Strategic")
    PRIZE = "prize", _("Prize")
    LOGISTICS = "logistics", _("Logistics")
    STYLE = "style", _("Style")
    HEALTH = "health", _("Health")
    BEVERAGE = "beverage", _("Beverage")
    ONLINE = "online", _("Online")


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="sponsor_logos")
    url = models.URLField()
    sponsor_type = models.CharField(choices=SponsorType.choices, max_length=20)

    def __str__(self):
        return self.name


class Merchandise(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="mechandise_images")
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.name
