import random
from collections import defaultdict

from task1 import Tracer
from task2 import Dumper

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


@Dumper(context=CONTEXT)
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


if __name__ == "__main__":
    func()
    funx("i")
    func()
    funx("i", n=3)
    func()
