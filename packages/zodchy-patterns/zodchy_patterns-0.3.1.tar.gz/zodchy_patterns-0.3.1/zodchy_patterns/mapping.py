import typing
import collections.abc

K = typing.TypeVar("K")
V = typing.TypeVar("V")


class DuplexMap(typing.Generic[K, V], typing.Mapping):
    """Double way mapping"""

    def __init__(self, data: collections.abc.Mapping[K, V]):
        self._data = data

    def __contains__(self, key: K) -> bool:
        return key in self._data

    def __getitem__(self, key: K) -> V:
        return self._data[key]

    def __iter__(self):
        yield from self._data

    def __len__(self) -> K:
        return len(self._data)

    def get(
        self,
        key: K,
        default: typing.Any | None = None
    ) -> V | typing.Any:
        return self._data.get(key, default)

    def __call__(self, value: V) -> K | None:
        for k, v in self._data.items():
            if v == value:
                return k
