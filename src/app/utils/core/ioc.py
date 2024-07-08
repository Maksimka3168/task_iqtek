from typing import TypeVar

T = TypeVar('T')


class IoC(object):

    def __init__(self):
        super().__setattr__('_values', {})

    def register(self, key, value):
        self._values[key] = value

    def __setattr__(self, key, value):
        self.register(key, value)

    def __getattr__(self, key) -> T:
        if key not in self._values:
            raise AttributeError(f"Key {key} is not registered.")

        attribute = self._values[key]
        return attribute(self) if callable(attribute) else attribute


ioc = IoC()
