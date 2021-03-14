from django.shortcuts import render


def homepage(request):

    context = {}

    return render(request, "base.html", context)