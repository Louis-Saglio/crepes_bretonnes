from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^accueil$', views.home),
    url(r'^article/(\d+)$', views.view_article),
    url(r'^articles/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles, name="articles"),
    url(r'^article$', views.redirige, name="article"),
    url(r'^accueil/(\d+)/argument2$', views.test_argument, name="toto"),
    url(r'^test_render/$', views.test_render),
    url(r'^calculatrice/(?P<nombre2>\d+)/(?P<nombre1>\d+)$', views.calculatrice, name="calto"),

]
