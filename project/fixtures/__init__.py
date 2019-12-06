import pytest


@pytest.fixture
def variable_factory(db):
    from persistent_settings.models import Variable

    def factory(value, name="FOO"):
        return Variable.objects.create(name=name, value=value)

    return factory
