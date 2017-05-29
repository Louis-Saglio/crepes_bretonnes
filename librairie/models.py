from django.db import models


class Auteur(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)

    def __str__(self):
        return self.nom.title() + ' ' + self.prenom.title()


class Categorie(models.Model):
    nom = models.CharField(max_length=25, null=False)

    def __str__(self):
        return self.nom


class Livre(models.Model):
    titre = models.CharField(max_length=50)
    nbr_pages = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey('Auteur')
    categorie = models.ManyToManyField('Categorie', through='LivreCategorie')

    def __str__(self):
        return self.titre.title() + ' de ' + self.auteur.__str__()


class LivreCategorie(models.Model):
    livre = models.ForeignKey('Livre')
    categorie = models.ForeignKey('Categorie')
    is_main_cat = models.BooleanField()
