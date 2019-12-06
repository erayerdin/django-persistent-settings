import logging
import pickle

from django.db import models

_LOGGER = logging.getLogger(__name__)


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

        _LOGGER.debug("Deleting `value_binary` kwarg...")
        kwargs.pop("value_binary", None)

        _LOGGER.debug("Serializing `value`...")
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

        _LOGGER.debug("Deserializing `value_binary`...")
        return pickle.loads(self.value_binary)

    @value.setter
    def value(self, v):
        """
        Serializes `value` into `value_binary`.
        """
        _LOGGER.debug("Serializing `value` into `value_binary`...")
        self.value_binary = pickle.dumps(v)
