import pytest
from django.core.management.base import CommandError


@pytest.mark.it("present variable")
def test_present_variable(variable_factory, command_factory):
    variable_factory("lorem")
    out = command_factory("delvar", "FOO")
    assert "successfully" in out.lower()


@pytest.mark.it("absent variable")
def test_absent_variable(db, command_factory):
    with pytest.raises(CommandError) as e:
        command_factory("delvar", "FOO")
        assert "does not exist" in e.value


@pytest.mark.it("absent variable | no error")
def test_no_error(db, command_factory):
    out = command_factory("delvar", "FOO", "--no-error")
    assert "does not exist" in out
