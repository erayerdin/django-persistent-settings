import pytest


@pytest.fixture
def variable_factory(db):
    from persistent_settings.models import Variable

    def factory(value, name="FOO"):
        return Variable.objects.create(name=name, value=value)

    return factory


@pytest.fixture
def request_obj(client):
    from django.urls import reverse

    return client.get(reverse("test")).wsgi_request
