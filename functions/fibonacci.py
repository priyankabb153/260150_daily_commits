def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = 1
    elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 10):  # testing
    print(n, "->", fib(n))


# recursion


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(3))

num = int(input())


def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(num):
    print(fibonacci(i))
