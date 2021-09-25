from django.db import models

class truthTable(models.Model):
    operation = models.CharField(max_length=100)

    def __str__(self):
        return self.operation