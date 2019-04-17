# inefficient sequence
# def fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
#
# for n in range(1, 50):
#     print(n, ":", fibonacci(n))

from functools import lru_cache
fibonacci_cache = dict()


@lru_cache(maxsize=1000)
def fibonacci(x):
    # Check for integer
    if type(x) != int:
        raise TypeError("x must be a positive integer")
    if x < 0:
        raise ValueError("x must be a positive integer")

    # if value is cached, return it
    if x in fibonacci_cache:
        return fibonacci_cache[x]

    # Compute nth term
    if x == 1:
        value = 1
    elif x == 2:
        value = 1
    elif x > 2:
        value = fibonacci(x-1) + fibonacci(x-2)

    # Cache the value and return it
    fibonacci_cache[x] = value
    return value


# for x in range(1, 201):
#     print(x, ":", fibonacci(x))

for x in range(1, 101):
    print(fibonacci(x+1)/fibonacci(x))
