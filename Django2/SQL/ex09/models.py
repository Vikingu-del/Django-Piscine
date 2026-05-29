from django.db import models


# Create your models here.
class Planets(models.Model):
    name = models.CharField(max_length=64, unique=True)
    climate = models.TextField(null=True, blank=True)
    diameter = models.IntegerField(null=True)
    orbital_period = models.IntegerField(null=True)
    population = models.BigIntegerField(null=True)
    rotation_period = models.IntegerField(null=True)
    surface_water = models.FloatField(null=True)
    terrain = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class People(models.Model):
    name = models.CharField(max_length=64)
    birth_year = models.CharField(max_length=32, null=True)
    gender = models.CharField(max_length=32, null=True)
    eye_color = models.CharField(max_length=32, null=True)
    hair_color = models.CharField(max_length=32, null=True)
    height = models.IntegerField(null=True)
    mass = models.FloatField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    homeworld = models.ForeignKey(
        Planets,
        on_delete=models.CASCADE,
        # to_field='name', # Normally should be this but because of the fixtures
        db_column="homeworld",
        null=True,  # also this
        blank=True,  # also this
    )

    def __str__(self):
        return self.name
