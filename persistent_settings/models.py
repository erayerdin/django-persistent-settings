import logging
import pickle

from django.db import models

_LOGGER = logging.getLogger(__name__)


class _VariableManager(models.Manager):
    """
    A special manager for `Variable` model overriding default Django manager.
    """

    def __getitem__(self, key: str):
        """
        Used for PersistentSettingsMiddleware.
        """
        return self.get(name=key).value


class _PickleField(models.BinaryField):
    """
    A field for marshalling with pickle.
    """

    def from_db_value(self, value, *args, **kwargs):  # pragma: no cover
        # kwargs has a key called "context" in dj1.11
        # kept for backwards compatibility
        if value is None:
            return None

        return pickle.loads(value)

    def to_python(self, value):  # pragma: no cover
        if isinstance(value, bytes) or value is None:
            return value

        return pickle.loads(value)

    def get_prep_value(self, value):  # pragma: no cover
        if value is None:
            return None

        return pickle.dumps(value)


class Variable(models.Model):
    """
    A single setting.
    """

    name = models.SlugField(unique=True, max_length=64)
    value = _PickleField(null=True)

    objects = _VariableManager()

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
