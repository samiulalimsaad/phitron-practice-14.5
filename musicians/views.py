from django.shortcuts import get_object_or_404, redirect, render

from musicians.form.album import AlbumForm
from musicians.form.musician import MusicianForm
from musicians.models.album import Album
from musicians.models.musician import Musician


def index(args):
    return redirect("/musicians")


def musician_list(request):
    musicians = Musician.objects.all()
    return render(request, "musician_list.html", {"musicians": musicians})


def album_list(request):
    albums = Album.objects.all()
    return render(request, "album_list.html", {"albums": albums})
