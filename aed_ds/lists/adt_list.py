from abc import ABC, abstractmethod
from aed_ds.lists.adt_iterator import Iterator

class List(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        """Returns true iff the lists contains no elements."""

    @abstractmethod
    def size(self) -> int:
        """Returns the number of elements in the lists."""

    @abstractmethod
    def get_first(self) -> object:
        """Returns the first element of the lists.

        Throws EmptyListException."""

    @abstractmethod
    def get_last(self) -> object:
        """Returns the last element of the lists.

        Throws EmptyListException."""

    @abstractmethod
    def get(self, position: int) -> object:
        """Returns the element at the specified position in the lists.

        Range of valid positions: 0, ..., size()-1."""

    @abstractmethod
    def find(self, element: object) -> bool:
        """Returns the position in the lists of the first occurrence of the
        specified element, or -1 if the specified element does not occur in the
        lists."""

    @abstractmethod
    def insert_first(self, element: object) -> None:
        """Inserts the specified element at the first position in the lists."""

    @abstractmethod
    def insert_last(self, element: object) -> None:
        """Inserts the specified element at the last position in the lists."""

    @abstractmethod
    def insert(self, element: object, position: int) -> None:
        """Inserts the specified element at the specified position in the lists.

        Range of valid positions: 0, ..., size().

        If the specified position is 0, insert corresponds to insertFirst.

        If the specified position is size(), insert corresponds to insertLast.

        Throws InvalidPositionException."""

    @abstractmethod
    def remove_first(self) -> object:
        """Removes and returns the element at the first position in the lists.

        Throws EmptyListException."""

    @abstractmethod
    def remove_last(self) -> object:
        """Removes and returns the element at the last position in the lists.

        Throws EmptyListException."""

    @abstractmethod
    def remove(self, position: int) -> object:
        """Removes and returns the element at the specified position in the
        lists.

        Range of valid positions: 0, ..., size()-1.

        Throws InvalidPositionException."""

    @abstractmethod
    def make_empty(self) -> None:
        """Removes all elements from the lists."""

    @abstractmethod
    def iterator(self) -> Iterator:
        """Returns an iterator of the elements in the lists (in proper
        sequence)."""
