from django.shortcuts import redirect, render

from musicians.models.musician import Musician


def index(args):
    return redirect("/musicians")


def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, "musician_list.html", {"musicians": musicians})
