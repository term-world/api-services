from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    user_id = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user_id} - {self.item.name}"
