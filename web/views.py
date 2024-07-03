from django.template import loader
from django.http import HttpRequest, HttpResponse

from core.logic import get_bamboos_with_min_michelin_stars
from core.models import Bamboo


def index(request: HttpRequest) -> HttpResponse:
    min_stars = request.GET.get("min_stars", 0)
    bamboos = get_bamboos_with_min_michelin_stars(min_stars)
    template = loader.get_template("web/index.html")
    context = {
        "bamboos": bamboos,
        "min_stars": min_stars
    }
    return HttpResponse(template.render(context, request))