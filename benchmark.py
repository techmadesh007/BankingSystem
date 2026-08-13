import bisect
import random
import timeit

from sortedcontainers import SortedDict


NUMBER_OF_INSERTIONS = 5000


def benchmark_bisect():
    setup = """
import bisect
import random

values = []
numbers = list(range(5000))
random.shuffle(numbers)
"""

    statement = """
for number in numbers:
    bisect.insort(values, number)
"""

    return timeit.timeit(
        stmt=statement,
        setup=setup,
        number=1
    )


def benchmark_sorted_dict():
    setup = """
import random
from sortedcontainers import SortedDict

values = SortedDict()
numbers = list(range(5000))
random.shuffle(numbers)
"""

    statement = """
for number in numbers:
    values[number] = number
"""

    return timeit.timeit(
        stmt=statement,
        setup=setup,
        number=1
    )


def run_benchmark():
    bisect_time = benchmark_bisect()
    sorted_dict_time = benchmark_sorted_dict()

    print("\n========================================")
    print("       WEEK 3 PERFORMANCE BENCHMARK")
    print("========================================")
    print(f"Number of insertions : {NUMBER_OF_INSERTIONS}")
    print()
    print(f"bisect.insort time   : {bisect_time:.6f} seconds")
    print(f"SortedDict time      : {sorted_dict_time:.6f} seconds")
    print()

    if bisect_time < sorted_dict_time:
        faster = "bisect.insort"
    else:
        faster = "SortedDict"

    print(f"Faster implementation: {faster}")
    print("========================================")

    return bisect_time, sorted_dict_time


if __name__ == "__main__":
    run_benchmark()