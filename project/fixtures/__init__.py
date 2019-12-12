import pytest


@pytest.fixture
def variable_factory(db):
    """
    Returns a Variable instance.
    """
    from persistent_settings.models import Variable

    def factory(value, name="FOO"):
        return Variable.objects.create(name=name, value=value)

    return factory


@pytest.fixture
def request_obj(client):
    from django.urls import reverse

    return client.get(reverse("test")).wsgi_request


@pytest.fixture
def template_factory():
    """
    Returns a Template factory.
    """

    from django import template

    def build_template_args(*args, **kwargs):
        args_string = " ".join(map(lambda a: '"{}"'.format(a), args))
        kwargs_string = " ".join(map(lambda k: '{}="{}"'.format(k, kwargs[k]), kwargs))
        return " ".join((args_string, kwargs_string))

    def factory(*args, **kwargs):
        load = kwargs.pop("load", "persistent_settings")
        tag_name = kwargs.pop("tag_name")
        wrapper = kwargs.pop("wrapper", "p")

        segments = (
            "{{% load {} %}}".format(load),
            "<{wrapper}>{{% {tag_name} {allargs} %}}</{wrapper}>".format(
                tag_name=tag_name,
                allargs=build_template_args(*args, **kwargs),
                wrapper=wrapper,
            ),
        )
        template_string = "\n".join(segments)
        return template.Template(template_string)

    return factory


@pytest.fixture
def context_factory():
    """
    Returns a Context factory to be used while rendering a Template instance.
    """

    from django import template

    def factory(**kwargs):
        return template.Context(kwargs)

    return factory
