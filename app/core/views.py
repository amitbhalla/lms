from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


@api_view(["GET"])
def api_root(request):
    context = {
        "API Root": {
            "Root": reverse("root", request=request),
            "API Root": reverse("api-root", request=request),
        },
    }
    return Response(context)
