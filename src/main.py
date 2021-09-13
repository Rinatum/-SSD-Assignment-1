import cmath
import random
import time
from collections import defaultdict

from task2 import dumper
from task3 import Tracer, Dumper, FilePrinter, TimeRanker
from task4 import ErrorHanler

CONTEXT = {"__runs": defaultdict(int)}


@Tracer(context=CONTEXT)
def func():
    """
    Some important documentation here
    :return: something important
    """
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += i ** 2


@dumper(context=CONTEXT)
def funx(a, n=2, m=5):
    """
    Some important documentation here
    :param a: important argument a
    :param n: important argument n
    :param m: important argument m
    :return: something important
    """
    print("I am ready to do serious stuff")
    max_val = float("-inf")
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


@Dumper(context=CONTEXT, printer=FilePrinter("test.txt"))
def solve_quadratic_equation(a, b, c):
    """
    (Adapted from https://www.javatpoint.com/python-quadratic-equation)
    The function that allows to fund roots of quadratic equation of the form
    ax^2 + bx + c = 0
    :param a:
    :param b:
    :param c:
    """

    discriminant = lambda a_, b_, c_: (b_ ** 2) - (4 * a_ * c_)

    # discriminant
    d = discriminant(a, b, c)

    # roots
    root_1 = (-b - cmath.sqrt(d)) / (2 * a)
    root_2 = (-b + cmath.sqrt(d)) / (2 * a)
    print(f"The solution : {root_1} ; {root_2}")

    return root_1, root_2


@Dumper(context=CONTEXT)
def pascal_triangle(n=5):
    """
    (Adapted from https://www.geeksforgeeks.org/python-program-to-print-pascals-triangle/)
    Print pascal triangle of n based on powers of 11 approach
    :param n: depth of pascal triangle
    """

    spacer = lambda n_, i_: " " * (n_ - i_)
    power = lambda i_: " ".join(map(str, str(11 ** i)))

    # iterarte upto n
    for i in range(n):
        # handle spaces
        print(spacer(n, i), end="")
        # compute powers of 11
        print(power(i))


@Dumper(context=CONTEXT, printer=FilePrinter("test.txt"))
def sleep(n):
    time.sleep(n)


ranker = TimeRanker(FilePrinter("test2.txt"))


@ranker
def kek():
    time.sleep(1)


@ranker
def kek2():
    time.sleep(2)


@ranker
def kek1():
    time.sleep(3)


@ErrorHanler(FilePrinter("exceptions.txt"))
@Dumper(CONTEXT)
def get_error():
    raise Exception("Oh")


if __name__ == "__main__":
    # task 1, 2
    func()
    funx("i")
    func()
    funx("i", n=3)
    pascal_triangle(3)
    solve_quadratic_equation(1, 2, 3)
    sleep(3)
    # task 3

    kek()
    kek1()
    kek2()
    ranker.log()

    # task4
    get_error()
