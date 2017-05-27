from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404

# Create your views here.


def home(request):
    """ Exemple de page HTML, non valide pour que l'exemple soit concis """
    text = """<h1>Bienvenue sur mon apprentissage !</h1>
              <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)


def view_article(request, id_article):
    if int(id_article) > 9:
        raise Http404
    return HttpResponse(f"Article {id_article}")


def list_articles(request, month, year):
    return HttpResponse(f"Article de {month} {year} {request.GET['ref']}")


def redirige(request):
    return redirect(home)


def test_argument(request, *argument):
    return HttpResponse(str(argument))


def test_render(request):
    a = [4, 'r', 88, 'ppml', True]
    return render(request, 'apprentissage/test_render.html', {'variable': 'rien de rien de rien', "liste": a})


def calculatrice(request, nombre1, nombre2):
    resultat = int(nombre1) + int(nombre2)
    return render(request, 'apprentissage/calculatrice.html', locals())
