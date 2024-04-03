from django.contrib import admin
from django.db import models

class Spell(models.Model):
    """Spells"""
    _id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1000, unique=True)
    school = models.CharField(max_length=1000)
    level = models.IntegerField(default=-1)
    casting_time = models.CharField(max_length=1000)
    range = models.CharField(max_length=1000)
    components = models.CharField(max_length=1000)
    duration = models.CharField(max_length=1000)
    description = models.TextField(max_length=5000)
    description_high = models.TextField(max_length=1000)
    book = models.CharField(max_length=50)
    favorite = models.BooleanField(null=True)
    # skipping several unused class fields ...
    notes = models.TextField(blank=True)
    clases = models.CharField(max_length=300)
    ritual = models.BooleanField()
    concentration = models.BooleanField()
    sound = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'spell'
        ordering = ['level', 'name']