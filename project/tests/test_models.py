import pytest


@pytest.mark.describe("Variable Model")
class TestVariable:
    @pytest.mark.it("value prop with types")
    def test_value_prop(self, variable_factory):
        v_int = variable_factory(5, "V_INT")
        v_float = variable_factory(5.5, "V_FLOAT")
        v_bool = variable_factory(True, "V_BOOL")
        v_str = variable_factory("bar", "V_STR")

        assert v_int.value == 5
        assert v_float.value == 5.5
        assert v_bool.value
        assert v_str.value == "bar"
