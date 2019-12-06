import pickle

from django.db import models


class _VariableManager(models.Manager):
    """
    A special manager for `Variable` model overriding default Django manager.
    """

    def create(self, **kwargs):
        """
        Creates a `Variable` instance.

        Serializes `value` to `value_binary` field using `pickle`.

        If no `value` is given, `None` is serialized.
        """

        kwargs.pop("value_binary", None)
        value = kwargs.pop("value", None)
        value_binary = pickle.dumps(value)

        return super().create(value_binary=value_binary, **kwargs)


class Variable(models.Model):
    """
    A single setting.
    """

    name = models.SlugField(primary_key=True, max_length=64)
    value_binary = models.BinaryField()

    objects = _VariableManager()

    class Meta:
        ordering = ("name",)

    @property
    def value(self):
        """
        Deserializes `value_binary` using `pickle`.
        """

        return pickle.loads(self.value_binary)
