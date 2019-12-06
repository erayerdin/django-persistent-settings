from django.db import models


class Variable(models.Model):
    """
    A single setting.
    """

    name = models.SlugField(primary_key=True, max_length=64)
    value = models.BinaryField()

    class Meta:
        ordering = ("name",)
