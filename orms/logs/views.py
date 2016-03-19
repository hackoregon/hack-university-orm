"""logs Views."""
from django.http import HttpResponse


def index(request):
    """Return the main page."""
    return HttpResponse("Hello, world. You're at the logs index.")
