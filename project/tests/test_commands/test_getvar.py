import pytest
from django.core.management.base import CommandError


@pytest.mark.it("present variable")
def test_present_variable(variable_factory, command_factory):
    variable_factory("lorem ipsum")
    out = command_factory("getvar", "FOO")
    assert "lorem ipsum" in out


@pytest.mark.it("absent variable")
def test_absent_variable(db, command_factory):
    with pytest.raises(CommandError) as e:
        command_factory("getvar", "FOO")
        assert "does not exist" in e.value


@pytest.mark.it("bash-style print out")
def test_bash_style(variable_factory, command_factory):
    variable_factory("lorem ipsum")
    out = command_factory("getvar", "FOO", "--bash-style")
    assert 'export FOO="lorem ipsum"' in out
