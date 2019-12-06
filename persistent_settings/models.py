from django.db import models


class Variable(models.Model):
    """
    A single setting.
    """

    name = models.CharField(primary_key=True)
    value = models.BinaryField()

    class Meta:
        ordering = ("name",)
