from unittest.mock import MagicMock

from code_flags.utils import Defer, Singleton, defer, package_attrs


def test_package_attrs():
    attrs = package_attrs[int]('answer_to_everything')
    obj = MagicMock()
    EXPECTED = 42
    assert not attrs.active(obj)
    attrs.put(obj, EXPECTED)
    assert attrs.active(obj)
    assert attrs.get(obj) == EXPECTED


def test_singleton():
    EXPECTED = 42

    class TestClass(Singleton):
        def __init__(self):
            self.value = EXPECTED

    inst1 = TestClass()
    inst2 = TestClass()
    assert inst1 is inst2
    assert inst1.value == EXPECTED
    assert inst2.value == EXPECTED


def test_singleton_clear():
    class TestClass(Singleton):
        pass

    inst1 = TestClass()
    TestClass.singleton_clear()
    inst2 = TestClass()
    assert inst1 is not inst2


def test_singleton_ensure_new():
    EXPECTED = 42

    class TestClass(Singleton):
        def __init__(self, value):
            self.value = value

    inst1 = TestClass.singleton_ensure_new(EXPECTED)
    inst2 = TestClass.singleton_ensure_new(EXPECTED * 2)
    assert inst1 is not inst2
    assert inst1.value == EXPECTED
    assert inst2.value == EXPECTED * 2


def test_singleton_revert_init():
    class TestClass(Singleton):
        pass

    inst1 = TestClass()
    TestClass.singleton_clear()
    TestClass.singleton_ensure_new()  # This will cause revert_init to be called
    assert inst1 is not TestClass()


def test_defer():
    class MyClass:
        def __init__(self, value):
            self.value = value

    EXPECTED = 42
    deferred_instance = Defer(MyClass, EXPECTED)
    instance = deferred_instance()
    assert instance.value == EXPECTED
    assert instance is deferred_instance.get_instance()


def test_defer_function():
    EXPECTED = 42

    class MyClass:
        def __init__(self, value):
            self.value = value

    deferred_instance = defer(MyClass, EXPECTED)
    instance = deferred_instance()
    assert instance.value == EXPECTED
    assert instance is deferred_instance.get_instance()
