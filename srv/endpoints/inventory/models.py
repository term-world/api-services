import pgtrigger
from django.db import models

@pgtrigger.register(
    pgtrigger.Trigger(
        name='decrement_item_qty_trigger',
        level=pgtrigger.Row,
        operation=pgtrigger.Update,
        when=pgtrigger.Before,
        func="""
        BEGIN
            IF NEW.item_qty = 0 THEN
                DELETE FROM inventory_inventory WHERE item_id = OLD.item_id;
            END IF;
            RETURN NEW;
        END;
        """
    )
)
class Inventory(models.Model):
    item_name = models.CharField(max_length=255)
    item_qty = models.FloatField()
    item_weight = models.FloatField()
    item_bulk = models.FloatField()
    item_consumable = models.BooleanField()
    item_bin = models.BinaryField()

    def __str__(self):
        return self.item_name