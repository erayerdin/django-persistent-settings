import logging

from persistent_settings import models
from persistent_settings.templatetags import register

_LOGGER = logging.getLogger(__name__)


@register.simple_tag(name="var")
def get_var(name, rit=True, rif=False, rin=None):
    """
    A template tag to render value of a variable.
    """

    _LOGGER.debug("Rendering value for `%s`...", name)

    variable = models.Variable.objects.get(name=name)
    value = variable.value

    if value is None:
        return rin

    if isinstance(value, bool):
        if value:
            return rit
        else:
            return rif

    return variable.value
