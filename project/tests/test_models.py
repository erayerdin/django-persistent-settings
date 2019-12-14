import pytest

from persistent_settings import models

""" @pytest.mark.describe("Variable Model")
class TestVariable:
    @pytest.mark.it("`value` prop with types")
    def test_value_prop(self, variable_factory):
        v_int = variable_factory(5, "V_INT")
        v_float = variable_factory(5.5, "V_FLOAT")
        v_bool = variable_factory(True, "V_BOOL")
        v_str = variable_factory("bar", "V_STR")

        assert v_int.value == 5
        assert v_float.value == 5.5
        assert v_bool.value
        assert v_str.value == "bar"

    @pytest.mark.it("`value_binary` update by value setter")
    def test_update_attr(self, variable_factory):
        v = variable_factory(5)
        v.value = 6
        v.save()
        assert v.value == 6

    @pytest.mark.it(
        "add support for `value` in `update_fields` kwarg on instance `save`"
    )
    def test_update_fields_value(self, variable_factory):
        v = variable_factory(5)
        v.value = 6
        v.save(update_fields=("value",))
        assert v.value == 6

    @pytest.mark.it("manager `create` method")
    def test_create(self, db):
        v = models.Variable.objects.create(name="FOO", value=5)
        assert v.value == 5

    @pytest.mark.it("queryset `update` method")
    def test_update(self, variable_factory):
        for i in range(2):
            variable_factory("bar", "FOO{}".format(i))

        variables = models.Variable.objects.filter(name__startswith="FOO")
        variables.update(value="baz")

        for v in variables:
            assert v.value == "baz"
 """
# all tests above are invalidated due to it is already being covered by standard
# implementation of BinaryField, which is implemented in models as `_PickleField`
# these are subject to removal


@pytest.mark.describe("Variable Model")
class TestVariable:
    @pytest.mark.it("Create with all types")
    def test_create(self, db):
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
