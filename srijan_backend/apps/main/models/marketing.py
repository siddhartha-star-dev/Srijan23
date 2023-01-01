from django.db import models


class Sponsor(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to="sponsor_logos")
    url = models.URLField()

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
