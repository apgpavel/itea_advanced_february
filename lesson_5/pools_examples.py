from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
import time
executor = ThreadPoolExecutor(max_workers=100)

# def sleeping(time_to_sleep):
#     time.sleep(time_to_sleep)
#     return time_to_sleep
#
# a = []
# for i in range(100):
#     a.append(executor.submit(sleeping, i))
#
# for result_future in as_completed(a):
#     print(result_future.result())


class A:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __mul__(self, other):
        return A(
            self._x * other._x,
            self._y * other._y
        )


a = A(1, 2)
b = A(3, 4)

print(a * b)