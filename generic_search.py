# Example from "Classic Computer Science Problems in Python" Chapter 2 by David Kopec

from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Generic, List, Callable, Set, Deque, Dict, Any, Optional
from typing_extensions import Protocol
from heapq import heappush, heappop

T = TypeVar('T')

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound="Comparable")

class Comparable(Protocol):
    def __eq__(self, other: Any) -> bool:
        ...
    
    def __lt__(self: C, other: C) -> bool:
        ...

    def __gt__(self: C, other: C) -> bool:
        return (not self < other) and self != other
    
    def __le__(self: C, other: C) -> bool:
        return self < other or self == other

    def __ge__(self: C, other: C) -> bool:
        return not self < other

def binary_contains(sequence: Sequence[C], key: C) -> bool:
    low: int = 0
    high: int = len(sequence) - 1
    while low <= high: # пока есть место для поиска
        mid: int = (low + high) // 2
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    return False

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container 

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()
    
    def __repr__(self) -> str:
        return repr(self._container)

class Node(Generic[T]):
    # Класс с помощью которого отслеживается переход из одного состояния
    # в другое (или из одного места лабиринта в другое) во время поиска.
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0,
        heuristic: float = 0.0) -> None:
        self.state: T = state
        self.parent: Optional[Node] = parent
        # Тип Optional указывает, что переменная может ссылаться на значение
        # параметризированного типа или на None.
        # Строка from __future__ import annotations позволяет объектам ссылаться
        # на самих себя в аннотациях типов своих методов.
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)


def dfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T],
    List[T]]) -> Optional[Node[T]]:
    '''Поиск в глубину (depth-first search)'''
    # frontier - то, что нам нужно проверить
    frontier: Stack[Node[T]] = Stack()
    frontier.push(Node(initial, None))
    # explored - то, где мы уже были
    explored: Set[T] = {initial}

    # продолжаем, пока есть что просматривать
    while not frontier.empty:
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state
        # если мы нашли искомое, заканичиваем
        if goal_test(current_state):
            return current_node
        # проверяем, куда можно двинуться дальше и что мы еще не исследовали
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None # все проверили, пути к целевой точке не нашли

def node_to_path(node: Node[T]) -> List[T]:
    path: List[T] = [node.state]
    # двигаемся назад от конца к началу
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path







if __name__ == "__main__":
    print(linear_contains([1, 5, 15, 20], 5)) # True
    print(binary_contains(["a", "d", "e", "f", "z"], "f")) # True
    print(binary_contains(["a", "d", "e", "f", "z"], "u")) # False
    
    