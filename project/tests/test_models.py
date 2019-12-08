import pytest


@pytest.mark.describe("Variable Model")
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
