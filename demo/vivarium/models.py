from django.db import models
from uuid import uuid4


class Snake(models.Model):
    id = models.UUIDField(default=uuid4.uuid(), primary_key=True)
    name = models.CharField(max_length=100)
    species = models.ForeignKey(Species, null=True)


class Species(models.Model):
    id = models.UUIDField(default=uuid4.uuid(), primary_key=True)
    name = models.CharField(max_length=100)
