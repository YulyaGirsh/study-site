from typing import NamedTuple
import random
from typing import List, Dict, Optional, Any, Union

point = (3, 5)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Person(NamedTuple):
    'Данные о человеке'
    name: str
    surname: str
    date: str
    country: str


Megan = Person('Megan', 'Jones', '1998-07-16', 'Bolivia')


# print(Megan.surname)
def get_even(lst=44):
    'Функция возвращает только чтные числа'
    even_lst = []
    if lst % 2 == 0:
        print(f'Число "{lst}" добавлено в список even_lst')
        even_lst.append(lst)


print(get_even.__doc__)
first: int = 100
second: int = 200


def add_numbers(a: int, b: Union[int, str, float] = None) -> int:
    return a + b


def list_upper(abc: List[str]):
    for elem in abc:
        print(elem.upper())


print(add_numbers(first))
# print(add_numbers([1, 45, 21, 8], [4, 5]))
e: Any
t: Optional[list] = [4,,456,87,65]
