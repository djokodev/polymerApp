from django.db import models

class Polymer(models.Model):
    polymer = models.CharField(max_length=128)
    timestamp = models.DateTimeField()
    end_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.polymer 