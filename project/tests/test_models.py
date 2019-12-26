import pytest

from persistent_settings import models


@pytest.mark.describe("Variable Model")
class TestVariable:
    @pytest.mark.it("Create with all types")
    def test_create_types(self, db):
        models.Variable.objects.create(value=5, name="V_INT")
        models.Variable.objects.create(value=5.5, name="V_FLOAT")
        models.Variable.objects.create(value=True, name="V_BOOL")
        models.Variable.objects.create(value="bar", name="V_STR")
        models.Variable.objects.create(value=None, name="V_NONE1")
        models.Variable.objects.create(name="V_NONE2")

    @pytest.mark.it("Retrieve with all types")
    def test_retrieve(self, variable_factory):
        v_int = variable_factory(5, "V_INT")
        v_float = variable_factory(5.5, "V_FLOAT")
        v_bool = variable_factory(True, "V_BOOL")
        v_str = variable_factory("bar", "V_STR")
        v_none = variable_factory(None, "V_NONE1")

        assert v_int.value == 5
        assert v_float.value == 5.5
        assert v_bool.value
        assert v_str.value == "bar"
        assert v_none.value is None

    @pytest.mark.it("`__str__`")
    def test_str(self, variable_factory):
        v = variable_factory(5)
        assert str(v) == "FOO"
