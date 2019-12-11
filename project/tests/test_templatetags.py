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

    @pytest.mark.it("Render if True")
    def test_render_if_true(self, template_factory, context_factory, variable_factory):
        variable_factory(True)
        template = template_factory(
            "FOO", tag_name=self.tag_name, rit="this is true"
        ).render(context_factory())
        assert "<p>this is true</p>" in template

    @pytest.mark.it("Render if True by settings")
    def test_render_if_true_settings(
        self, template_factory, context_factory, variable_factory, settings
    ):
        setattr(settings, "DPS_TEMPLATE_TRUE_DEFAULT", "this is true by settings")
        variable_factory(True)
        template = template_factory("FOO", tag_name=self.tag_name).render(
            context_factory()
        )
        assert "<p>this is true by settings</p>" in template

    @pytest.mark.it("Render if False")
    def test_render_if_false(self, template_factory, context_factory, variable_factory):
        variable_factory(False)
        template = template_factory(
            "FOO", tag_name=self.tag_name, rif="this is false"
        ).render(context_factory())
        assert "<p>this is false</p>" in template

    @pytest.mark.it("Render if None")
    def test_render_if_none(self, template_factory, context_factory, variable_factory):
        variable_factory(None)
        template = template_factory(
            "FOO", tag_name=self.tag_name, rin="this is none"
        ).render(context_factory())
        assert "<p>this is none</p>" in template
