import pytest

from core.utils.params import bool_from_request, cast_bool_from_str


@pytest.mark.parametrize('value', [' true ', '\tYES\n', ' ON ', ' 1 '])
def test_boolean_accepts_surrounding_whitespace(value):
    assert cast_bool_from_str(value) is True
    assert bool_from_request({'enabled': value}, 'enabled', False) is True


@pytest.mark.parametrize('value', [' false ', '\tNO\n', ' OFF ', ' 0 '])
def test_boolean_false_accepts_surrounding_whitespace(value):
    assert cast_bool_from_str(value) is False
    assert bool_from_request({'enabled': value}, 'enabled', True) is False


def test_empty_boolean_remains_invalid():
    with pytest.raises(ValueError):
        cast_bool_from_str('   ')
