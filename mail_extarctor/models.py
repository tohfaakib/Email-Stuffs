from django.db import models

from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Extractor(models.Model):
    email_list = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return str(self.pk)
