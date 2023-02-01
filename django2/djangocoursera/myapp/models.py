from django.db import models
from django.db import models

class Menu(models.Model):
    item_name=models.CharField(max_length=100)
    cuisine=models.CharField(max_length=100)
    price=models.IntegerField()
    available=models.BooleanField(default=True)

    

    def __str__(self):
        return self.name+' : '+self.cuisine
