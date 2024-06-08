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
                DELETE FROM inventory_inventory WHERE item_id = OLD.id;
            END IF;
            RETURN NEW;
        END;
        """
    )
)
class Inventory(models.Model):
    item_name = models.CharField(max_length=225, unique=True)
    item_qty = models.FloatField(default=1.0)
    item_weight = models.FloatField(default=1.0)
    item_bulk = models.FloatField(default=1.0)
    item_consumable = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name