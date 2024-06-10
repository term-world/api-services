import pgtrigger
from datetime import datetime
from django.db import models

@pgtrigger.register(
    pgtrigger.Trigger(
        name = "omnipresence_update_is_active",
        level = pgtrigger.Statement,
        operation = pgtrigger.Update | pgtrigger.Insert,
        when = pgtrigger.After,
        func = f"""
            INSERT INTO omnipresence_omnipresencemodel (username, charname, working_dir, last_active, is_active)
            SELECT
                username AS username,
                charname AS charname,
                working_dir AS working_dir
            VALUES (username, charname, working_dir, NOW(), True)
            WHERE last_active < NOW() - INTERVAL '30 MINUTES'
            ON CONFLICT
            DO UPDATE SET
                last_active = NOW(),
                is_active = True
        """
    )
)
class OmnipresenceModel(models.Model):

    username = models.CharField(max_length = 255)
    charname = models.CharField(max_length = 255, unique = True)
    working_dir = models.CharField(max_length = 512)
    last_active = models.DateTimeField(auto_now_add = True)
    is_active = models.BooleanField(default = True)

    class Meta:
        triggers = [
            pgtrigger.Trigger(
                name = "omnipresence_update_is_active",
                level = pgtrigger.Statement,
                operation = pgtrigger.Update | pgtrigger.Insert,
                when = pgtrigger.After,
                func = f"""
                    INSERT INTO omnipresence_omnipresencemodel (username, charname, working_dir, last_active, is_active)
                    SELECT
                        username AS username,
                        charname AS charname,
                        working_dir AS working_dir
                    VALUES (username, charname, working_dir, NOW(), True)
                    WHERE last_active < NOW() - INTERVAL '30 MINUTES'
                    ON CONFLICT
                    DO UPDATE SET
                        last_active = NOW(),
                        is_active = True
                """
            )
        ]


    def as_dict(self):
        result = {}
        fields = self._meta.fields
        for field in fields:
            result[field.name] = getattr(self, field.name)
        return result
