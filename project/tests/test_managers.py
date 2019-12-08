import pytest

from persistent_settings import models


@pytest.mark.describe("Overriding `_VariableManager`'s Default Methods")
class TestOverrideVariableManager:
    @pytest.mark.it("`create` method")
    def test_create(self, db):
        v = models.Variable.objects.create(name="FOO", value=5)
        assert v.value == 5

    @pytest.mark.it("`update` method")
    def test_update(self, variable_factory):
        for i in range(2):
            variable_factory("bar", "FOO{}".format(i))

        variables = models.Variable.objects.filter(name__startswith="FOO")
        variables.update(value="baz")

        for v in variables:
            assert v.value == "baz"
