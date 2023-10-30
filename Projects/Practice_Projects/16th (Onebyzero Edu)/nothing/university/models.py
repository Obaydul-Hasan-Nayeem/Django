from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    # established = models.DateField()

    def __str__(self):
        return self.name
