"""
URL configuration for musicians project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from musicians.views import album_list, edit_album, edit_musician, index, musician_list

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index, name="index"),
    path("musicians/", musician_list, name="musician_list"),
    path("albums/", album_list, name="album_list"),
    path("edit/musician/<int:musician_id>/", edit_musician, name="edit_musician"),
    path("edit/album/<int:album_id>/", edit_album, name="edit_album"),
]
