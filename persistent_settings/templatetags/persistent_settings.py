from persistent_settings import models
from persistent_settings.templatetags import register


@register.simple_tag
def get_var(name):
    """
    A template tag to render value of a variable.
    """

    variable = models.Variable.objects.get(name=name)
    return variable.value
