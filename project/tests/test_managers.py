import pytest

from persistent_settings import models


@pytest.mark.describe("Overriding `_VariableManager`'s Default Methods")
class TestOverrideVariableManager:
    @pytest.mark.it("`create` method")
    def test_create(self, db):
        v = models.Variable.objects.create(name="FOO", value=5)
        assert v.value == 5
