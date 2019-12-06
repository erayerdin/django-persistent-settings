import pytest


@pytest.mark.it("Get Variable from request...")
def test_get(variable_factory, request_obj):
    variable_factory(5)
    assert request_obj.persistent_settings["FOO"] == 5
