from django.db import models


class OrganisingTeamMember(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team_images")
    designation = models.CharField(max_length=100)
    linkedin = models.URLField()
    github = models.URLField()
    instagram = models.URLField(blank=True, null=True)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Developers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="developers_images")
    designation = models.CharField(max_length=100)
    linkedin = models.URLField()
    github = models.URLField()
    instagram = models.URLField(blank=True, null=True)
    contact = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Notification(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.title
