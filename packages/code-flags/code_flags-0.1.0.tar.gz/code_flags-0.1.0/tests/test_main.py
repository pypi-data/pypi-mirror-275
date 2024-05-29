from unittest.mock import MagicMock

import pytest

from code_flags.loaders import ProxyLoader
from code_flags.main import initialize
from code_flags.stores import ProxyStore, get_store
from code_flags.stores.sqlite import SQLiteStore


@pytest.fixture
def mock_loader():
    return MagicMock()


@pytest.fixture
def mock_store():
    return MagicMock()


@pytest.fixture(autouse=True)
def reset_proxy():
    ProxyLoader.singleton_clear()
    ProxyStore.singleton_clear()


def test_initialize_with_custom_loader_and_store(mock_loader, mock_store):
    # Initialize with custom loader and store
    initialize(mock_loader, mock_store)

    # Assert that ProxyLoader and ProxyStore are properly integrated
    assert isinstance(ProxyLoader(object()), ProxyLoader)
    assert ProxyStore(object())._store is mock_store


def test_initialize_with_custom_loader(mock_loader):
    # Initialize with custom loader
    initialize(mock_loader)

    # Assert that ProxyLoader and StoreLoader are properly integrated
    assert ProxyLoader(object())._loader is mock_loader


def test_initialize_with_no_custom_loader_or_store():
    # Initialize with no custom loader or store
    initialize()

    # Assert that ProxyLoader and StoreLoader are properly integrated with default store
    default_store = get_store()
    assert isinstance(default_store, ProxyStore)
    assert isinstance(default_store._store, SQLiteStore)
