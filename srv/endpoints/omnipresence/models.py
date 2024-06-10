import pgtrigger
from datetime import datetime
from django.db import models

class OmnipresenceModel(models.Model):

    username = models.CharField(max_length = 255)
    charname = models.CharField(max_length = 255, unique = True)
    working_dir = models.CharField(max_length = 512)
    last_active = models.DateTimeField(auto_now = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        triggers = [
            pgtrigger.Trigger(
                name = "update_character_activity",
                operation = pgtrigger.Update,
                when = pgtrigger.Before,
                func = """
                    NEW.is_active = True; RETURN NEW;
                """
            )
        ]

    def as_dict(self):
        result = {}
        fields = self._meta.fields
        for field in fields:
            result[field.name] = getattr(self, field.name)
        return result
