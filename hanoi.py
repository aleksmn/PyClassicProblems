from typing import TypeVar, Generic, List
T = TypeVar('T')

# Задача Ханойские башни
# Есть башни А В и С, 3 диска с нанизаны на башню А.
# Самый широкий диск (1) находится внизу, самый узкий (3) - вверху.
# Задача состоит в том, чтобы переместить три диска по одному
# с башни А на башню С. Диск большего размера никогда не может
# располагаться поверх диска меньшего размера. 

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

# Определим башни как объекты Stack и заполним первую из них дисками

num_discs: int = 3
tower_a: Stack[int] = Stack()
tower_b: Stack[int] = Stack()
tower_c: Stack[int] = Stack()
for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)