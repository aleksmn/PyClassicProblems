'''
Прошу прощения, что только два задания.
На остальных либо мозг закипает, либо
Какая-то проблема, которую я пытаюсь решить
несколько часов. 
Надеюсь, что всё, что ниже, будет более
менее читаемо.
'''

from __future__ import annotations
from typing import Dict, Generator
from functools import lru_cache
import time 
import os
import random


# Вспомогательные функции и переменные

memo: Dict[int, int] = {0: 0, 1: 1} # Для функции fib3
cls = lambda: os.system('cls')


def get_sec() -> float:
    '''
    Возвращает прошедшие секунды
    с момента запуска программы.
    '''
    return time.time()


def get_func_from_name(name: str):
    '''
    Возвращает функцию от её названия в виде строки
    из глобального диапозона имён.
    '''
    return globals()[name]


# Упражение 1
TASK_1 = '''\
Напишите еще одну функцию, которая вычясляет n-й элемент последовательности
Фибоначи, используя метод вашей со6ственной разра6отки. Напишите
модульные тесты, которые оценивали бы правильность этой функции и ее про-
изводителыюсть, по сравнению с другими версиями, представленными в этой
главе.
'''

def fibCustom(n: int) -> int:
    '''
    Написана мной.
    Принимает любое позитивное число.
    Возвращает значение из последовательности
    Чибоначи позиции n.
    '''
    
    if n < 0:
        raise ValueError("Function accepts only positive values")
    elif n < 2:
        return n
    else:
        return fibCustom(n-1) + fibCustom(n-2)


def fib1(n: int) -> int: # Она из учебника и постоянно выдает ошибки.
    return fib1(n - 1) + fib1(n - 2)


def fib2(n: int) -> int:
    if n < 2: # базовый случай
        return n
    return fib2(n - 2) + fib2(n - 1)
    # рекурсивный случай


def fib3(n: int) -> int:
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2) # мемоизация
    return memo[n]


@lru_cache(maxsize=None)
def fib4(n: int) -> int: #такое же определение, как в fib2()
    if n < 2: # базовый случай
        return n
    return fib4(n - 2) + fib4(n - 1) # рекурсивный случай


def fib5(n: int) -> int:
    if n == 0: return n # специальный случай
    last: int = 0 # начальное значение fib(0)
    next: int = 1 # начальное значение fib(l)
    for _ in range(1, n):
        last, next = next, last + next
    return next


def fib6(n: int) -> Generator[int, None, None]:
    yield 0 # специальный случай
    if n > 0: yield 1 # специальный случай
    last: int = 0 #начальное значение fib(0)
    next: int = 1 #начальное значение fib(1)
    for _ in range(last, n):
        last, next = next, last + next
        yield next # главный этап генерации




def one_fib_test(func: callable, times: int=10, input: int=10) -> dict:
    '''
    Отдельное тестирование одной функции "семейства" fib.
    Выдает словарь с результатами теста
    '''
    res = {'all' : None, 'low': None, 'high': None, 'mid': None, 'exceptions count': 0, 'recursion error': False}
    time = []
    for i in range(times):
        on_start = get_sec()
        try:
            func(input)
        except Exception:
            res['exceptions count'] += 1
        except RecursionError:
            res.update['recursion error'] = True
        on_finish = get_sec() - on_start
        time.append(on_finish)

    res['all'] = time
    res['low'] = min(time)
    res['high'] = max(time)
    res['mid'] = sum(time) / len(time)
    return res


def all_fib_test(to_test=('fibCustom', 'fib1', 'fib2', 'fib3', 'fib4', 'fib5', 'fib6'), input=25) -> None:
    '''
    Тестирует функции fib.
    Думаю, что потом стоит доработать.
    '''
    cls()
    print(TASK_1)
    print("Начинаем тестировать функции fib...")

    for name in to_test:
        print("Тестируем {}".format(name))
        print("Ввод: {}".format(input))
        res = one_fib_test(get_func_from_name(name), input=input)
        print("Все время: {}".format(res['all']))
        print("Максимальное Время: {}, среднее время: {}, минимальное время {}. Общее количество ошибок: {}, ошибка рекурсии: {}".format(res['high'], res['mid'], res['low'], res['exceptions count'], res['recursion error']))
        results.update({name : res})

    print("Нажмите ESC, чтобы продолжить...")
    keyboard.wait('esc')
    main()
       

# Упражнение 2
TASK_2='''\
Продемонстрируйте преимущество в производительности бинарного поиска
по сравнению с линейным поиском, создав список из миллиона чисел и определив,
сколько времени потребуется созданным в этой главе функциям linear contains() и binary_contains() для поиска в нем различных чисел.
'''
def get_randnum_seq(min: int=0, max: int=100, length: int=1000000) -> sequence:
    '''
    Генерируем список, заполненный случайными числами.
    '''
    return [random.randint(min, max) for _ in range(length)]


def linear_contains(sequence: iterable, key_num: int) -> bool:
    '''
    Линейный поиск в последовательности.
    '''
    for num in sequence:
        if num == key_num:
            return True
    return False


def binary_contains(sequence: list, key_num: int) -> bool:
    '''
    Бинарный поиск в последовательности.
    '''
    low = 0
    high = len(sequence) - 1
    while (low <= high):
        mid = (low + high) // 2
        if sequence[mid] < key_num:
            low = mid + 1
        elif sequence[mid] > key_num:
            high = mid - 1
        else:
            return True
    return False


def contains_test():
    '''
    Сравнение линейного и бинарного поиска.
    '''
    cls()
    test_count = 100
    params = Min, Max, Length = 0, 100, 1000000
    
    print(TASK_2)
    print("Тестируем линейный и бинарный поиск\nс последовательностью из {} случайных чисел от {} до {}.".format(Length, Min, Max))
    print("Создаем последовательность...")
    sequence = get_randnum_seq(*params)
    print("Начинаем тестировать линейный поиск {} раз...".format(test_count))
    
    linear_res = []
    for _ in range(test_count):
        input = random.randint(Min-Min//2, Max+Max//2)
        start_time = get_sec()
        linear_contains(sequence, input)
        end_time = get_sec() - start_time
        linear_res.append(end_time)

    print("\nРезультат:")
    print("\tМаксимальное время: {0:.3f}. Минимальное {1:.3f}, среднее {2:.3f}.".format(max(linear_res), min(linear_res), sum(linear_res)/len(linear_res)))

    print('\nНачинаем тестировать бинарный поиск {} раз...'.format(test_count))
    print('Упорядовачиваем последовательность...')
    print('\t\t(может занять время)')
    sequence.sort()

    binary_test = []
    for _ in range(test_count):
        input = random.randint(Min-Min//2, Max+Max//2)
        start_time = get_sec()
        linear_contains(sequence, input)
        end_time = get_sec() - start_time
        binary_test.append(end_time)

    print("\nРезультат:")
    print("\tМаксимальное время: {0:.3f}. Минимальное {1:.3f}, среднее {2:.3f}.".format(max(binary_test), min(binary_test), sum(binary_test)/len(binary_test)))


    # Не знаю, почему линейный оказался лучше. Даже при большем разнообразии чисел он быстрее.

    print("Нажмите ESC, чтобы продолжить...")
    keyboard.wait('esc')
    main()


def main():
    # pygame.init()
    while (True):
        cls()
        print("Введите номер упражнения: ")
        print("[1] - Решение упражнения 1")
        print("[2] - Решения упражнения 2")
        print("[3] - Выйти")
        print(">> ", end='')

        try:
            ans = int(input())
            if ans == 3:
                break
            {1:all_fib_test, 2:contains_test}[ans]()
            break
        except (KeyError, ValueError):
            continue


if (__name__ == "__main__"):
    main()