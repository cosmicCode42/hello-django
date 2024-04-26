from django.db import models

# Create your models here.


class Item(models.Model):
    # schema for the Item database
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    # this will show the item's name instead of 'Item Object (x)'
    def __str__(self):
        return self.name
