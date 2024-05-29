import pytest

from code_flags.flag import Flag, FlagGroup


@pytest.fixture
def empty_flag_group():
    return FlagGroup()


def test_flag_creation(empty_flag_group):
    # Test creating a new flag
    flag_name = 'test_flag'
    default_value = False
    flag = empty_flag_group.get_or_create(flag_name, default_value)

    assert isinstance(flag, Flag)
    assert flag.name == flag_name
    assert flag.enabled is None
    assert flag.default == default_value
    assert flag in empty_flag_group.flags


def test_flag_existence(empty_flag_group):
    # Test checking flag existence
    flag_name = 'test_flag'
    default_value = False
    empty_flag_group.get_or_create(flag_name, default_value)

    assert flag_name in empty_flag_group
    assert 'non_existent_flag' not in empty_flag_group


def test_flag_retrieval(empty_flag_group):
    # Test retrieving an existing flag
    flag_name = 'test_flag'
    default_value = False
    empty_flag_group.get_or_create(flag_name, default_value)

    retrieved_flag = empty_flag_group.get(flag_name)

    assert isinstance(retrieved_flag, Flag)
    assert retrieved_flag.name == flag_name
    assert retrieved_flag.enabled is None
    assert retrieved_flag.default == default_value


def test_flag_upsert(empty_flag_group):
    # Test updating an existing flag
    flag_name = 'test_flag'
    default_value = False
    empty_flag_group.get_or_create(flag_name, default_value)

    new_enabled_value = True
    new_default_value = True
    updated_flag = empty_flag_group.upsert(
        flag_name, new_enabled_value, new_default_value
    )

    assert isinstance(updated_flag, Flag)
    assert updated_flag.name == flag_name
    assert updated_flag.enabled == new_enabled_value
    assert updated_flag.default == new_default_value
    assert updated_flag in empty_flag_group.flags


def test_flag_methods_with_non_existent_flag(empty_flag_group):
    # Test flag methods behavior when flag doesn't exist
    non_existent_flag_name = 'non_existent_flag'

    # Check flag existence
    assert non_existent_flag_name not in empty_flag_group

    # Attempt to retrieve the flag
    with pytest.raises(Exception):
        empty_flag_group.get(non_existent_flag_name)

    # Attempt to update the flag
    updated_flag = empty_flag_group.upsert(non_existent_flag_name, True, True)
    assert updated_flag in empty_flag_group.flags
