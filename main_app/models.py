from django.db import models


class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rarity = models.CharField(max_length=50)
    radiation_level = models.FloatField()
    value = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Anomaly(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    danger_level = models.IntegerField()
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Stalker(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=50)
    artifacts_collected = models.ManyToManyField(Artifact, related_name='stalkers')

    def __str__(self):
        return self.name