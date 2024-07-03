from django.db import models

class Bamboo(models.Model):
    species = models.CharField(max_length=200)
    michelin_stars = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.species