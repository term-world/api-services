from django.db import models

class OmnipresenceModel(models.Model):

    name = models.CharField(max_length = 255)
    char = models.CharField(max_length = 255)
    cwd = models.CharField(max_length = 512)

    def __str__(self):
        return "f{self.name} ({self.char}): {self.cwd}"
