from unittest.mock import MagicMock

import pytest

from code_flags.mark import (
    FlagGroup,
    flag,
    flag_state_attr,
    is_enabled,
    is_feature_flagged,
    mark,
)


@pytest.fixture
def mock_flag_group():
    return MagicMock(spec=FlagGroup)


def test_mark(mock_flag_group):
    obj = MagicMock()
    flag_name = 'test_flag'

    assert not is_feature_flagged(obj, flag_name)
    mark(obj, flag_name)
    assert is_feature_flagged(obj, flag_name)


def test_is_enabled(mock_flag_group):
    obj = MagicMock()
    flag_name = 'test_flag'
    mock_flag_group.get.return_value = MagicMock(default=False, enabled=None)
    mock_flag_group.__contains__.return_value = True
    flag_state_attr.put(obj, mock_flag_group)

    # Flag is not present in store, default to False
    assert not is_enabled(obj, flag_name)

    # Flag is present in store, default to True
    mock_flag_group.get.return_value = MagicMock(default=False, enabled=True)
    assert is_enabled(obj, flag_name)


def test_flag_decorator(mock_flag_group):
    flag_name = 'test_flag'
    mock_flag_group.get.return_value = MagicMock(default=False, enabled=True)
    mock_flag_group.get_or_create.return_value = MagicMock(
        default=False, enabled=True
    )
    mock_flag_group.__contains__.return_value = True

    # Define a function to be decorated

    def test_function():
        return True

    flag_state_attr.put(test_function, mock_flag_group)

    test_caller = flag(flag_name)(test_function)
    # Flag should be marked and function should be decorated
    assert is_feature_flagged(test_function, flag_name)
    assert is_enabled(test_function, flag_name)
    assert test_caller() is True

    # Function should return False if flag is disabled
    mock_flag_group.get.return_value = MagicMock(default=False, enabled=False)
    assert not test_caller()

    # Define a function to be decorated with custom on_disabled behavior
    def on_disabled():
        return False

    def test_function_with_custom_behavior():
        return True

    mock_flag_group.get.return_value = MagicMock(default=False, enabled=True)
    flag_state_attr.put(test_function_with_custom_behavior, mock_flag_group)
    test_caller_custom = flag(flag_name, on_disabled=on_disabled)(
        test_function_with_custom_behavior
    )
    # Flag should be marked and function should be decorated
    assert is_feature_flagged(test_function_with_custom_behavior, flag_name)
    assert is_enabled(test_function_with_custom_behavior, flag_name)
    assert test_caller_custom() is True

    # Function should return False if flag is disabled
    mock_flag_group.get.return_value = MagicMock(default=False, enabled=False)
    assert not test_caller_custom()
