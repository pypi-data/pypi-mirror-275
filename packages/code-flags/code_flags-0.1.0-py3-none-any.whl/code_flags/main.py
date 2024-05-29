from code_flags.loaders import Loader, ProxyLoader
from code_flags.loaders.helpers import initialize_store
from code_flags.loaders.store import StoreLoader
from code_flags.stores import ProxyStore, Store, get_store


def initialize(loader: Loader | None = None, store: Store | None = None):
    store = ProxyStore(store or get_store())
    if loader is None:
        loader = StoreLoader(store)
    loader = ProxyLoader(loader)
    initialize_store(loader, store)


def reset():
    ProxyLoader.singleton_clear()
    ProxyStore.singleton_clear()
