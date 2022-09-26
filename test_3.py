import re
import pytest
from pytest_bdd import given, then, parsers, scenarios

scenarios('./myfeatures/feature_3.feature')

@pytest.fixture
def foo():
    return {}
@given(parsers.re(r"a background step with multiple lines:\n(?P<data>.+)", flags=re.DOTALL))
def _(foo, data):
    assert data == "one\ntwo"
@given('foo has a value "bar"')
def _(foo):
    foo["bar"] = "bar"
    return foo["bar"]
@given('foo has a value "dummy"')
def _(foo):
    foo["dummy"] = "dummy"
    return foo["dummy"]
@given('foo has no value "bar"')
def _(foo):
    assert foo["bar"]
    del foo["bar"]
@then('foo should have value "bar"')
def _(foo):
    assert foo["bar"] == "bar"
@then('foo should have value "dummy"')
def _(foo):
    assert foo["dummy"] == "dummy"
@then('foo should not have value "bar"')
def _(foo):
    assert "bar" not in foo