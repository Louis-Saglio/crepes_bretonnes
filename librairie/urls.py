from django.conf.urls import url

from librairie import views

urlpatterns = [

    url(r'^accueil$', views.accueil, name="accueil")

]
