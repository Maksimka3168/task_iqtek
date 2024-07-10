from typing import TypeVar, Type, Any

T = TypeVar('T')


class IoC:
    def __init__(self):
        self._values = {}

    def register(self, key: Type[T], value: Any):
        self._values[key] = value

    def set(self, key: Type[T], value: Any):
        self.register(key, value)

    def get(self, key: Type[T]) -> T:
        if key not in self._values:
            raise AttributeError(f"Key {key} is not registered.")
        attribute = self._values[key]
        return attribute() if callable(attribute) else attribute


ioc = IoC()
