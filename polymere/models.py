from django.db import models

class Reaction(models.Model):
    reactif = models.CharField(max_length=26)
    produit = models.CharField(max_length=26)
    start = models.DateTimeField()
    end = models.DateTimeField(auto_now_add=True)


