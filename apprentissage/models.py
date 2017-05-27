from django.db import models


class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=25)
    contenu = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")

    def __str__(self):
        return self.titre
