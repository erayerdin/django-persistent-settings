import pytest


@pytest.mark.describe("`var` tag")
class TestGetVarTag:
    tag_name = "var"

    @pytest.mark.it("Only with variable name")
    def test_only_var_name(self, template_factory, context_factory, variable_factory):
        variable_factory(5, "V_INT")
        t_int = template_factory("V_INT", tag_name=self.tag_name).render(
            context_factory()
        )

        variable_factory(5.5, "V_FLOAT")
        t_float = template_factory("V_FLOAT", tag_name=self.tag_name).render(
            context_factory()
        )

        variable_factory(False, "V_BOOL")
        t_bool = template_factory("V_BOOL", tag_name=self.tag_name).render(
            context_factory()
        )

        variable_factory("lorem", "V_STR")
        t_str = template_factory("V_STR", tag_name=self.tag_name).render(
            context_factory()
        )

        assert "<p>5</p>" in t_int
        assert "<p>5.5</p>" in t_float
        assert "<p>False</p>" in t_bool
        assert "<p>lorem</p>" in t_str

    def test_render_if_true(self, template_factory, context_factory, variable_factory):
        variable_factory(True)
        template = template_factory(
            "FOO", tag_name=self.tag_name, rit="this is true"
        ).render(context_factory())
        assert "<p>this is true</p>" in template
