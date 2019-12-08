import logging
import pickle

from django.db import models

_LOGGER = logging.getLogger(__name__)


def _change_value_kwarg(kwargs):
    """
    Changes `value` to `value_binary` by serializing it.
    """

    _LOGGER.debug("Removing `value_binary`...")
    kwargs.pop("value_binary", None)

    _LOGGER.debug("Serializing `value` to `value_binary`...")
    value = kwargs.pop("value", None)
    value_binary = pickle.dumps(value)
    kwargs["value_binary"] = value_binary
    return kwargs


class _VariableQuerySet(models.QuerySet):
    """
    A special queryset for `Variable` model overriding default Django queryset.
    """

    def update(self, **kwargs):
        _change_value_kwarg(kwargs)
        return super().update(**kwargs)


class _VariableManager(models.Manager):
    """
    A special manager for `Variable` model overriding default Django manager.
    """

    def __getitem__(self, key: str):
        """
        Used for PersistentSettingsMiddleware.
        """
        return self.get(name=key).value

    def get_queryset(self):
        _LOGGER.debug("Initializing `_VariableQuerySet`...")
        return _VariableQuerySet(self.model, using=self._db)

    def create(self, **kwargs):
        _change_value_kwarg(kwargs)
        return super().create(**kwargs)


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

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None,
    ):
        if update_fields:
            update_fields = list(update_fields)

            try:
                value_index = update_fields.index("value")
                _LOGGER.debug(
                    "Replacing `value` in `update_fields` kwarg with `value_binary`..."
                )
                update_fields[value_index] = "value_binary"
            except ValueError:  # pragma: no cover
                _LOGGER.debug("No `value` in `update_fields` kwarg.")

        return super().save(
            force_insert=force_insert,
            force_update=force_update,
            using=using,
            update_fields=update_fields,
        )
