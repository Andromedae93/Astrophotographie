from django.shortcuts import render

from .models import Photo


# Fonction(s) liées à l'accueil de la partie Astrophoto
def AccueilPhotographies(request):
    return render(request, 'AccueilPhotographies.html')


# Fonction(s) liées à la partie photo planétaire
def Planetaire(request):
    return render(request, 'Planetaire.html')


# Fonction(s) liées à la partie photo CP
def Galaxies(request):
    galaxies = Photo.objects.filter(Type_objet="Galaxie").order_by("-Date")

    return render(request, 'Galaxie.html', {"galaxies": galaxies})


def NebuleusesDiffuses(request):
    nebuleuses_diffuses = Photo.objects.filter(Type_objet="Nébuleuse Diffuse").order_by("-Date")

    return render(request, 'Nebuleuse_Diffuse.html', {"nebuleuses_diffuses": nebuleuses_diffuses})


def NebuleusesPlanetaires(request):
    nebuleuses_planetaires = Photo.objects.filter(Type_objet="Nébuleuse Planétaire").order_by("-Date")

    return render(request, 'Nebuleuse_Planetaire.html', {"nebuleuses_planetaires": nebuleuses_planetaires})


def AmasGlobulaires(request):
    amas_globulaires = Photo.objects.filter(Type_objet="Amas Globulaire").order_by("-Date")

    return render(request, 'Amas_Globulaire.html', {"amas_globulaires": amas_globulaires})


def AmasOuverts(request):
    amas_ouverts = Photo.objects.filter(Type_objet="Amas Ouvert").order_by("-Date")

    return render(request, 'Amas_Ouvert.html', {"amas_ouverts": amas_ouverts})


# Fonction(s) liées à d'autres objets
def Autres(request):
    return render(request, 'Autres.html')
