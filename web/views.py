from django.template import loader
from django.http import HttpRequest, HttpResponse

from web.models import Bamboo


def index(request: HttpRequest) -> HttpResponse:
    min_stars = request.GET.get("min_stars", 0)
    bamboos = Bamboo.objects.filter(michelin_stars__gte=min_stars).order_by("-michelin_stars")
    template = loader.get_template("web/index.html")
    context = {
        "bamboos": bamboos,
        "min_stars": min_stars
    }
    return HttpResponse(template.render(context, request))