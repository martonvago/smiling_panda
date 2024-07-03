from core.models import Bamboo
from django.db.models import QuerySet

def get_bamboos_with_min_michelin_stars(min_stars: int) -> QuerySet:
    return Bamboo.objects.filter(michelin_stars__gte=min_stars).order_by("-michelin_stars")
