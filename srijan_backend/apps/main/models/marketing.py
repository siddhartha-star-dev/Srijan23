from django.db import models
from django.utils.translation import gettext_lazy as _


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="sponsor_logos")
    url = models.URLField()
    sponsor_type = models.CharField(max_length=20, null=True)
    sponsor_category = models.CharField(max_length=20, null=True)

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
