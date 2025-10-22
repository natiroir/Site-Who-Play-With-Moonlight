from django.shortcuts import render
from .config import MENU_LINKS


def get_context():
    """Retourne le contexte commun pour toutes les pages"""
    return {
        'menu_links': MENU_LINKS,
    }


def home(request):
    context = get_context()
    return render(request, 'home.html', context)


def actualite(request):
    context = get_context()
    return render(request, 'actualite.html', context)


def reproducteur(request):
    context = get_context()
    return render(request, 'reproducteur.html', context)


def chiots(request):
    context = get_context()
    return render(request, 'chiots.html', context)


def communaute(request):
    context = get_context()
    return render(request, 'communaute.html', context)


def contact(request):
    context = get_context()
    return render(request, 'contact.html', context)
