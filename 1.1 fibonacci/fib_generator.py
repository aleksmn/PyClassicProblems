from typing import Generator

def fib(n: int) -> Generator[int, None, None]:
    yield 0
    if n > 0: yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next # главный этап генерации

if __name__ == "__main__":
    print(fib(10))
    for i in fib(10):
        print(i)
