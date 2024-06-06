from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    item_qty = models.FloatField()
    item_weight = models.FloatField()
    item_bulk = models.FloatField()
    item_consumable = models.BooleanField()
    item_bin = models.BinaryField()

    def __str__(self):
        return self.name

class Inventory(models.Model):
    user_id = models.IntegerField()
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.user_id} - {self.item.name}"
