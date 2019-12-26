import pytest
from django.core.management.base import CommandError

from persistent_settings import models


@pytest.mark.it("create variable | exists")
def test_create_variable_exists(db, command_factory):
    command_factory("setvar", "FOO", "lorem ipsum")
    assert models.Variable.objects.filter(name="FOO").exists()


@pytest.mark.it("create variable | out")
def test_create_variable_out(db, command_factory):
    out = command_factory("setvar", "FOO", "lorem ipsum").lower()
    assert "successfully" in out
    assert "created" in out


@pytest.mark.it("update variable | value")
def test_update_variable_value(variable_factory, command_factory):
    variable_factory("lorem")
    command_factory("setvar", "FOO", "ipsum")
    assert models.Variable.objects.get(name="FOO").value == "ipsum"


@pytest.mark.it("update variable | out")
def test_update_variable_out(variable_factory, command_factory):
    variable_factory("lorem")
    out = command_factory("setvar", "FOO", "ipsum").lower()
    assert "successfully" in out
    assert "updated" in out


@pytest.mark.it("no update")
def test_no_update(variable_factory, command_factory):
    variable_factory("lorem")
    with pytest.raises(CommandError) as e:
        command_factory("setvar", "FOO", "ipsum", "-n")
        assert "already exists" in e.value


@pytest.mark.it("value | none")
def test_value_none(db, command_factory):
    command_factory("setvar", "FOO")
    assert models.Variable.objects.get(name="FOO").value is None


@pytest.mark.it("type | int")
def test_type_int(db, command_factory):
    command_factory("setvar", "FOO", "5", "--type", "int")
    assert models.Variable.objects.get(name="FOO").value == 5


@pytest.mark.it("type | float")
def test_type_float(db, command_factory):
    command_factory("setvar", "FOO", "5.5", "--type", "float")
    assert models.Variable.objects.get(name="FOO").value == 5.5


@pytest.mark.it("type | bool | true")
def test_type_bool_true(db, command_factory):
    true_vals = ("true", "True", "t", "T", "y", "Y", "yes", "Yes")
    # actually, anything is valid True

    for i in range(len(true_vals)):
        t_val = true_vals[i]
        name = "FOO{}".format(i)
        command_factory("setvar", name, t_val, "--type", "bool")
        assert models.Variable.objects.get(name=name).value  # is true


@pytest.mark.it("type | bool | false")
def test_type_bool_false(db, command_factory):
    false_vals = ("false", "False", "f", "F", "n", "N", "no", "No")
    # all these result in False

    for i in range(len(false_vals)):
        f_val = false_vals[i]
        name = "FOO{}".format(i)
        command_factory("setvar", name, f_val, "--type", "bool")
        assert not models.Variable.objects.get(name=name).value  # is false
