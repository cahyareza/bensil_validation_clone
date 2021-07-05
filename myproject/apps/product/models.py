from django.db import models

class ProductUnique(models.Model):
    title = models.CharField(max_length=10)
    unique = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.unique}"