from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=80)
    instructions = models.TextField()
    author = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=80)
    quantity = models.FloatField()
    unit = models.CharField(max_length=30, blank=True)
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
