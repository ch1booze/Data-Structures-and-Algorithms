import random
from typing import List, Any


def binary_search(lst: List[Any], search_item: Any):
    start = 0
    stop = len(lst) - 1
    steps = 0
    while start <= stop:
        middle = (start + stop) // 2
        steps += 1
        print(f"{start} - {middle} - {stop}")

        if lst[middle] == search_item:
            print(f"{steps=}")
            return f"{search_item} found in index {middle}."

        if lst[middle] < search_item:
            start = middle + 1
        else:
            stop = middle - 1

    print(f"{steps=}")
    return f"{search_item} is not in list."


with open("names.txt", "r") as file:
    names = file.read()
names = names.splitlines()

print(binary_search(names, 'zeinab'))
