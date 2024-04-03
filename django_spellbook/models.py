from django.contrib import admin
from django.db import models


def ordinal(n):
    suffixes = {1: "st", 2: "nd", 3: "rd"}
    return str(n) + ("th" if 10 < abs(n) < 14 else suffixes.get(abs(n) % 10, "th"))


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

    @property
    @admin.display(description="Level", ordering="level")
    def pretty_level(self):
        return "Cantrip" if self.level == -1 else ordinal(self.level)

    @property
    @admin.display(description="School", ordering="school")
    def pretty_school(self):
        return self.school.split()[0]

    @property
    @admin.display(description="Components", ordering="components")
    def short_components(self):
        return self.components.split("(")[0].strip()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = "spell"
        ordering = ["level", "name"]
