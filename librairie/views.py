from django.shortcuts import render, get_object_or_404
from librairie.models import Livre


def accueil(request):
    return render(request, 'librairie/accueil.html')


def get_livre(request, identifiant):
    livre = get_object_or_404(Livre, id=identifiant)
