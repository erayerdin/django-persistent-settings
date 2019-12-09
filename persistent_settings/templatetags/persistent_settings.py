from persistent_settings import models
from persistent_settings.templatetags import register


@register.simple_tag(name="var")
def get_var(name, rit="True"):
    """
    A template tag to render value of a variable.
    """

    variable = models.Variable.objects.get(name=name)
    value = variable.value

    if isinstance(value, bool):
        if value:
            return rit

    return variable.value
