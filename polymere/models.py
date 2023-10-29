from django.db import models

class Polymer(models.Model):
    polymer = models.CharField(max_length=128)
    timestamp = models.DateTimeField()

    def __str__(self):
        return self.polymer 