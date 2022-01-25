from django.shortcuts import render
from .models import GeeksModel  # relative import of forms

# Create your views here.
# pass id attribute from urls


def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["data"] = GeeksModel.objects.get(id=id)
    return render(request, "detail_view.html", context)
