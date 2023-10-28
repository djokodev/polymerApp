from django.db import models

class Reaction(models.Model):
    reactif = models.CharField()
    produit = models.CharField()
    start = models.DateTimeField()
    end = models.DateTimeField(auto_now_add=True)


