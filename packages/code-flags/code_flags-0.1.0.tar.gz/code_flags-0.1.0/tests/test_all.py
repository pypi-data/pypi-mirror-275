import asyncio
from pathlib import Path

import pytest

from code_flags.loaders.toml import TomlLoader
from code_flags.main import initialize, reset
from code_flags.mark import async_flag, flag
from code_flags.stores.sqlalchemy import SQLAlchemyStore
from code_flags.stores.sqlite import SQLiteStore

RESOURCES_DIR = Path(__file__).parent / 'resources'


@pytest.fixture(autouse=True)
def reset_fixture():
    reset()


@pytest.fixture
def sqlite_store():
    # Create a SQLiteStore with an in-memory database
    return SQLiteStore(':memory:')


@pytest.fixture
def toml_file():
    # Create a temporary TOML file with feature flags
    return RESOURCES_DIR / 'integration.toml'


@pytest.fixture
def toml_loader(toml_file):
    # Create a TomlLoader with the temporary TOML file
    return TomlLoader(toml_file)


def test_integration_sqlite(sqlite_store, toml_loader):
    # Initialize the system with the SQLiteStore and TomlLoader
    initialize(loader=toml_loader, store=sqlite_store)

    # Define a synchronous function decorated with flag
    @flag('feature1')
    def sync_function():
        return 'Feature 1 is enabled'

    # Define an asynchronous function decorated with async_flag
    @async_flag('feature2')
    async def async_function():
        return 'Feature 2 is enabled'

    # Define a synchronous function decorated with flag, with custom behavior when disabled
    @flag('feature3', on_disabled=lambda: 'Feature 3 is disabled')
    def custom_behavior_function():
        return 'This function should not be called because feature3 is always disabled'

    # Call the decorated functions and verify their behavior
    assert sync_function() == 'Feature 1 is enabled'
    assert asyncio.run(async_function()) == 'Feature 2 is enabled'
    assert custom_behavior_function() == 'Feature 3 is disabled'


RESOURCES_DIR = Path(__file__).parent / 'resources'


@pytest.fixture
def sqlalchemy_store():
    # Create a SQLAlchemyStore with an in-memory SQLite database
    return SQLAlchemyStore('sqlite:///:memory:')


def test_integration(sqlalchemy_store, toml_loader):
    # Initialize the system with the SQLAlchemyStore and TomlLoader
    initialize(loader=toml_loader, store=sqlalchemy_store)

    # Define a synchronous function decorated with flag
    @flag('feature1')
    def sync_function():
        return 'Feature 1 is enabled'

    # Define an asynchronous function decorated with async_flag
    @async_flag('feature2')
    async def async_function():
        return 'Feature 2 is enabled'

    # Define a synchronous function decorated with flag, with custom behavior when disabled
    @flag('feature3', on_disabled=lambda: 'Feature 3 is disabled')
    def custom_behavior_function():
        return 'This function should not be called because feature3 is always enabled'

    # Call the decorated functions and verify their behavior
    assert sync_function() == 'Feature 1 is enabled'
    assert asyncio.run(async_function()) == 'Feature 2 is enabled'
    assert custom_behavior_function() == 'Feature 3 is disabled'
