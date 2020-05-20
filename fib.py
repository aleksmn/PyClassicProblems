from typing import Dict, List, Callable
from functools import lru_cache
import time

def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)
# RecursionError: maximum recursion depth exceeded

def fib2(n: int) -> int:
    if n < 2:  # базовый случай
        return n
    return fib2(n - 1) + fib2(n - 2)
# подходит только для n < 50

# Использование мемоизации
memo: Dict[int, int] = {0: 0, 1: 1} # базовые случаи
 
def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # мемоизация
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2:  # базовый случай
        return n
    return fib4(n - 1) + fib4(n - 2)  # рекурсивный случай 


def fib5(n: int) -> int:
    """Итеративный метод"""
    if n == 0: return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


def test_func(func):
    # get starting time
    start = time.time()
    try:
        for _ in range(100):
            func(100)
    except RecursionError:
        return "Recursion error"
    taken_time = time.time() - start
    taken_time = round(taken_time, 9)
    return taken_time



if __name__ == "__main__":
    functions_to_test: List[Callable] = [fib3, fib4, fib5]
    for i in range(len(functions_to_test)):
        func_name = functions_to_test[i].__name__
        func_time = test_func(functions_to_test[i])

        print(f'Function: {func_name}, time: {func_time} seconds.')

    
